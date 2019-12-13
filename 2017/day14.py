from day10 import *


# pt 1

KEY = 'stpzcrnm'


def convert_key(key):
    return [knot_hash(key + '-' + str(i)) for i in range(128)]


def h_to_b(h):
    return '{:04b}'.format(int(h, 16))


def count_used(key):
    count = 0
    for i in range(128):
        for h in knot_hash(key + '-' + str(i)):
            count += h_to_b(h).count('1')
    return count


# pt 2
def key_to_grid(key):
    grid = []
    for i in range(128):
        grid.append(''.join([h_to_b(h) for h in knot_hash(key + '-' + str(i))]))
    return grid


def grid_to_graph(grid):
    graph = {}
    for i, row in enumerate(grid):
        for j, square in enumerate(row):
            if square == '1':
                graph[(i, j)] = graph.get((i, j), [])
                if j+1 < len(row) and grid[i][j+1] == '1':
                    graph[(i, j)] += [(i, j+1)]
                    graph[(i, j+1)] = graph.get((i, j+1), []) + [(i, j)]
                if i+1 < len(grid) and grid[i+1][j] == '1':
                    graph[(i, j)] += [(i+1, j)]
                    graph[(i+1, j)] = graph.get((i+1, j), []) + [(i, j)]
    return graph


def grouping(graph, square):
    to_do = graph[square]
    group = {square}
    while to_do:
        temp_square = to_do.pop()
        if temp_square not in group:
            group.add(temp_square)
            to_do += graph[temp_square]
    return group


def count_regions(graph):
    num_regions = 0
    squares = set(graph.keys())
    while squares:
        square = squares.pop()
        region = grouping(graph, square)
        num_regions += 1
        squares -= region
    return num_regions


def main():
    # pt 1
    print(count_used(KEY))

    # pt 2
    grid = key_to_grid(KEY)
    graph = grid_to_graph(grid)
    print(count_regions(graph))


if __name__ == '__main__':
    main()




