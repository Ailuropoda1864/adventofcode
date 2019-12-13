day = 11

###############################
from read_input import *

input_string = get_input_string(day)
sn = int(input_string)


def calculate_power(x, y, sn):
    rack_ID = x + 10
    power = (rack_ID * y + sn) * rack_ID
    return power // 100 % 10 - 5


def create_grid(sn):
    return {(x, y): calculate_power(x, y, sn) for x in range(1, 301)
            for y in range(1, 301)}


def sum_grid(grid, x, y, size=3):
    return sum(
        grid[(i, j)] for i in range(x, x + size) for j in range(y, y + size))


def sum_row(grid, x_range, y):
    return sum(grid[(x, y)] for x in x_range)


def sum_col(grid, x, y_range):
    return sum(grid[(x, y)] for y in y_range)


def find_largest_power(grid, size=3):
    max_power = -float('inf')
    final_x, final_y = None, None
    for x in range(1, 302 - size):
        for y in range(1, 302 - size):
            total_power = sum_grid(grid, x, y, size)
            if total_power > max_power:
                final_x, final_y = x, y
                max_power = total_power
    return final_x, final_y, max_power


def find_largest_power2(grid):
    cache = grid.copy()
    max_power = max(cache.values())
    final_x, final_y, final_size = None, None, None

    for size in range(2, 301):
        for (x, y), v in cache.items():
            max_x, max_y = x + size - 1, y + size - 1
            if max_x <= 300 and max_y <= 300:
                total_power = (v
                               + sum_row(grid, range(x, max_x + 1), max_y)
                               + sum_col(grid, max_x, range(y, max_y)))
                cache[(x, y)] = total_power
                if total_power > max_power:
                    final_x, final_y = x, y
                    final_size = size
                    max_power = total_power

    return final_x, final_y, final_size


if __name__ == '__main__':
    from time import time
    grid = create_grid(sn)
    # Part One
    print(find_largest_power(grid))
    # Part Two
    start = time()
    print(find_largest_power2(grid))
    print(time()-start)



