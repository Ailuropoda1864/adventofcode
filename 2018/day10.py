day = 10

###############################
from read_input import *
import re


class Point:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def move(self, seconds=1):
        self.x += self.v_x * seconds
        self.y += self.v_y * seconds
        return self


def parse_input_file(file):
    pattern = re.compile(
        r'position=< ?(-?[0-9]+),  ?(-?[0-9]+)> velocity=< ?(-?[0-9]+),  ?(-?[0-9]+)>')
    with open(file) as f:
        return [Point(*map(int, pattern.match(line).groups())) for line in f]


def get_grid(points):
    x_min, x_max = min(point.x for point in points), max(point.x for point in points)
    y_min, y_max = min(point.y for point in points), max(point.y for point in points)
    return x_min, x_max, y_min, y_max, (x_max - x_min) * (y_max - y_min)


def move_points(points, seconds=1):
    return [point.move(seconds) for point in points]


def fastforward(file, seconds=1):
    points = parse_input_file(file)

    time = 0
    min_size = get_grid(points)[-1]

    while True:
        size = get_grid(points)[-1]
        if size > min_size:
            return time-1, move_points(points, -1)
        else:
            points = move_points(points, seconds)
            time += seconds
            min_size = size


def plot_points(points):
    x_min, x_max, y_min, y_max, _ = get_grid(points)
    grid = [['.' for x in range(x_max-x_min+1)] for y in range(y_max-y_min+1)]
    for point in points:
        grid[point.y-y_min][point.x-x_min] = '#'
    for row in grid:
        print(''.join(row))


if __name__ == '__main__':
    time, points = fastforward('input.txt')
    # Part One
    plot_points(points)
    # Part Two
    print(time)
