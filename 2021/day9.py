DAY = 9

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return tuple(tuple(map(int, list(line))) for line in input_string.splitlines())


def find_low_points(heightmap):
    y_len = len(heightmap)
    x_len = len(heightmap[0])
    low_points = []
    low_point_positions = []

    for y, line in enumerate(heightmap):
        for x, num in enumerate(line):
            up, down, left, right = True, True, True, True
            if y - 1 >= 0 and num >= heightmap[y - 1][x]:
                up = False
            if y + 1 < y_len and num >= heightmap[y + 1][x]:
                down = False
            if x - 1 >= 0 and num >= heightmap[y][x - 1]:
                left = False
            if x + 1 < x_len and num >= heightmap[y][x + 1]:
                right = False
            if all([up, down, left, right]):
                low_points.append(num)
                low_point_positions.append((x, y))
    return low_points, low_point_positions


def part1(heightmap):
    low_points, _ = find_low_points(heightmap)
    return sum(low_points) + len(low_points)


def get_next_visits(heightmap, x, y):
    to_visit = set()
    if x - 1 >= 0:
        to_visit.add((x - 1, y))
    if x + 1 < len(heightmap[0]):
        to_visit.add((x + 1, y))
    if y - 1 >= 0:
        to_visit.add((x, y - 1))
    if y + 1 < len(heightmap):
        to_visit.add((x, y + 1))
    return to_visit


def part2(heightmap):
    _, low_point_positions = find_low_points(heightmap)
    basins = []
    for x, y in low_point_positions:
        basin = {
            (x, y),
        }
        visited = {
            (x, y),
        }
        to_visit = get_next_visits(heightmap, x, y)
        while len(to_visit) > 0:
            next_x, next_y = to_visit.pop()
            if (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                if heightmap[next_y][next_x] != 9:
                    basin.add((next_x, next_y))
                    next_visits = get_next_visits(heightmap, next_x, next_y)
                    to_visit |= next_visits
        basins.append(basin)
    basin_sizes = [len(basin) for basin in basins]
    basin_sizes.sort()
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]


if __name__ == "__main__":
    heightmap = parse_input(test=False)
    # Part 1
    print(part1(heightmap))
    # Part 2
    print(part2(heightmap))
