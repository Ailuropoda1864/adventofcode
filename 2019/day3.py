day = 3

###############################
from read_input import *
from collections import namedtuple

input_string = get_input_string(day)
input_list = input_string.splitlines()


# Part One
Point = namedtuple('Point', ['x', 'y'])


def trace_wire(wire, segment):
    dist = int(segment[1:])
    p = wire[-1]
    if segment[0] == 'R':
        return wire + [Point(p.x + i, p.y) for i in range(1, dist + 1)]
    elif segment[0] == 'L':
        return wire + [Point(p.x - i, p.y) for i in range(1, dist + 1)]
    elif segment[0] == 'U':
        return wire + [Point(p.x, p.y + i) for i in range(1, dist + 1)]
    elif segment[0] == 'D':
        return wire + [Point(p.x, p.y - i) for i in range(1, dist + 1)]


def add_wire(wire_string):
    wire = [Point(0, 0)]
    for s in wire_string.split(','):
        wire = trace_wire(wire, s)
    return wire


def get_distance(point):
    return abs(point.x) + abs(point.y)


wire1 = add_wire(input_list[0])
wire2 = add_wire(input_list[1])
crosses = set(wire1) & set(wire2)


print(min(get_distance(c) for c in crosses if c != Point(0, 0)))


# Part Two
print(min(wire1.index(c) + wire2.index(c) for c in crosses if c != Point(0, 0)))
