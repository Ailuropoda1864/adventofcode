DAY = 2

###############################
from read_input import *


def parse_input(test=True):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return [line.split() for line in input_string.splitlines()]


def part1(instr):
    horizontal_pos = 0
    depth = 0
    for direction, step_str in instr:
        step = int(step_str)
        if direction == "forward":
            horizontal_pos += step
        elif direction == "down":
            depth += step
        elif direction == "up":
            depth -= step
        else:
            raise f"Direction not recognize: {direction}"
    return horizontal_pos * depth


def part2(instr):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for direction, x_str in instr:
        x = int(x_str)
        if direction == "down":
            aim += x
        elif direction == "up":
            aim -= x
        elif direction == "forward":
            horizontal_pos += x
            depth += aim * x
        else:
            raise f"Direction not recognize: {direction}"
    return horizontal_pos * depth


if __name__ == "__main__":
    input_list = parse_input(test=False)
    # Part 1
    print(part1(input_list))
    # Part 2
    print(part2(input_list))
