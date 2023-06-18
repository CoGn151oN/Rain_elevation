import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Graph:
    @staticmethod
    def plot(arr: list) -> None:
        """
        Displays 3D animated graph of region parcel elevation above sea level.
        :return: None
        """
        values = np.array(arr)
        # Create grid
        rows = np.arange(values.shape[1])
        cols = np.arange(values.shape[0])[::-1]  # Reverse cols so display isn't mirrored
        x, y = np.meshgrid(rows, cols)

        # Create 3D figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot_surface(x, y, values, cmap='viridis')
        ax.set_xlabel('Rows')
        ax.set_ylabel('Cols')
        ax.set_zlabel('Elevation')

        # animation
        def rotate(angle):
            ax.view_init(elev=28, azim=angle)

        def animate(frame):
            rotate(frame)

        autorun_anim = FuncAnimation(fig, animate, frames=np.arange(0, 360, 1.5), interval=100)

        plt.show()
