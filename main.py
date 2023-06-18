from graph import Graph

if __name__ == '__main__':
    stdin = """3 4
    25 37 45 49
    51 12 34 25
    94 83 27 29
    10000"""

    # preprocess
    row, col = [int(n) for n in stdin.split()[:2]]
    elevation = [list(map(int, i.split())) for i in stdin.split("\n")[1:-1]]
    precipitation = float(stdin.split()[-1])

    Graph.plot(elevation)









