day = 17

###############################
from read_input import *
import re

input_string = get_input_string(day)
input_string = get_input_string_from_file('test.txt')
split_input = input_string.splitlines()

def parse_input(split_input):
    pattern = re.compile(r'([xy])=([0-9]+), ([xy])=([0-9]+)..([0-9]+)')
    clays = set()
    for line in split_input:
        var1, value1, var2, value2a, value2b = pattern.match(line).groups()
        value1, value2a, value2b = int(value1), int(value2a), int(value2b)
        if var1 == 'x':
            clays |= {(value1, y) for y in range(value2a, value2b + 1)}
        elif var1 == 'y':
            clays |= {(x, value1) for x in range(value2a, value2b + 1)}
    return clays


def get_y_range(clays):
    return min(c[1] for c in clays), max(c[1] for c in clays)


def part1(split_input):
    clays = parse_input(split_input)
    min_y, max_y = get_y_range(clays)
    x = 500
    y = min_y
    water = set()
    to_visit = {(x, y)}
    while to_visit:
        x, y = to_visit.pop()
        if (x, y) in clays:


            to_visit.extend([(x - 1, y), (x + 1, y)])
        else:
            water.add((x, y))
            next_tile = {(x, y + 1)}


            to_visit.add((x, y + 1))







if __name__ == '__main__':


