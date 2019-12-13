day = 17

###############################
from read_input import *
import re

input_string = get_input_string(day)
#input_string = get_input_string_from_file('test.txt')
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


def part1(clays):
    min_y, max_y = get_y_range(clays)
    x = 500
    water = set()
    water_sources = [(x, min_y)]

    while water_sources:

        next_water_sources = []
        for water_source in water_sources:
            x, y = water_source
            if y > max_y:
                break
            water.add(water_source)
            next_tile = (x, y + 1)
            appended = False
            if next_tile in clays or next_tile in water:
                # go left
                next_tile = (x - 1, y)
                while next_tile not in clays:
                    if ((next_tile[0], next_tile[1] + 1) in clays
                            or (next_tile[0], next_tile[1] + 1) in water):
                        water.add(next_tile)
                        next_tile = (next_tile[0] - 1, next_tile[1])
                    else:
                        next_water_sources.append(next_tile)
                        appended = True
                        break
                # go right
                next_tile = (x + 1, y)
                while next_tile not in clays:
                    if ((next_tile[0], next_tile[1] + 1) in clays or
                            (next_tile[0], next_tile[1] + 1) in water):
                        water.add(next_tile)
                        next_tile = (next_tile[0] + 1, next_tile[1])
                    else:
                        next_water_sources.append(next_tile)
                        appended = True
                        break

                if not appended:
                    next_water_sources.append((water_source[0], water_source[1] - 1))

            else:
                next_water_sources.append(next_tile)
        water_sources = next_water_sources[:]
        i += 1

    return water


def plot(water, clays):
    min_x = min(min(w[0] for w in water), min(c[0] for c in clays))
    max_x = max(max(w[0] for w in water), max(c[0] for c in clays))
    min_y = min(min(w[1] for w in water), min(c[1] for c in clays))
    max_y = max(max(w[1] for w in water), max(c[1] for c in clays))

    for y in range(min_y, max_y + 1):
        output = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in water:
                output += '~'
            elif (x, y) in clays:
                output += '#'
            else:
                output += '.'
        print(output)


# def plot(clays):
#     min_x = min(c[0] for c in clays)
#     max_x = max(c[0] for c in clays)
#     min_y = min(c[1] for c in clays)
#     max_y = max(c[1] for c in clays)
#
#     for y in range(min_y, max_y + 1):
#         output = ''
#         for x in range(min_x, max_x + 1):
#             if (x, y) in clays:
#                 output += '#'
#             else:
#                 output += '.'
#         print(output)


if __name__ == '__main__':
    clays = parse_input(split_input)
    water = part1(clays)
    print(len(water))
    plot(water, clays)



