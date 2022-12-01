DAY = 1

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    elfs = []
    total_calorie = 0
    for line in input_string.splitlines() + [""]:
        if line == "":
            elfs.append(total_calorie)
            total_calorie = 0
        else:
            total_calorie += int(line)
    return elfs


def part1(elfs):
    return max(elfs)


def part2(elfs):
    return sum(sorted(elfs)[-3:])


if __name__ == "__main__":
    elfs = parse_input(test=False)
    # Part 1
    print(part1(elfs))
    # Part 2
    print(part2(elfs))
