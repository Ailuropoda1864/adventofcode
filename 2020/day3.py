day = 3

###############################
from functools import reduce
from operator import mul

from read_input import *

input_string = get_input_string(day)
# input_string = read_file('test.txt')


# Part One
def read_map(input_string):
    return {
        (x, y): symbol
        for y, line in enumerate(input_string.splitlines())
        for x, symbol in enumerate(line)
    }


def map_dimension(input_string):
    length = input_string.rstrip('\n').count('\n') + 1
    width = len(input_string.split('\n')[0])
    return width, length


def part1(input_string, x_rule=3, y_rule=1):
    x_max, y_max = map_dimension(input_string)
    tree_map = read_map(input_string)
    tree_count = 0
    x, y = 0, 0
    while y < y_max:
        if tree_map[(x % x_max, y)] == '#':
            tree_count += 1
        x += x_rule
        y += y_rule
    return tree_count


# Part Two
def part2(input_string):
    return reduce(mul,
                  (part1(input_string, x_rule, y_rule)
                   for x_rule, y_rule in (
                       (1, 1),
                       (3, 1),
                       (5, 1),
                       (7, 1),
                       (1, 2)
                   )
                   ))


if __name__ == '__main__':
    print(part1(input_string))
    print(part2(input_string))

