day = 3

###############################
from functools import reduce
from operator import mul

from read_input import *


input_string = get_input_string(day)
# input_string = read_file('test.txt')

input_list = input_string.splitlines()

# Part One
def part1(input_list, x_rule=3, y_rule=1):
    y_max = len(input_list)
    x_max = len(input_list[0])
    hits = 0
    x, y = 0, 0
    while y < y_max:
        if input_list[y][x % x_max] == '#':
            hits += 1
        x += x_rule
        y += y_rule
    return hits


# Part Two
def part2(input_list):
    return reduce(mul,
                  (part1(input_list, x_rule, y_rule)
                   for x_rule, y_rule in (
                       (1, 1),
                       (3, 1),
                       (5, 1),
                       (7, 1),
                       (1, 2)
                   )
                   ))


if __name__ == '__main__':
    print(part1(input_list))
    print(part2(input_list))

