DAY = 4

###############################
from read_input import *


def get_sections(elf):
    start, end = tuple(map(int, elf.split("-")))
    return set(range(start, end + 1))


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return [
        list(map(get_sections, pair.split(","))) for pair in input_string.splitlines()
    ]


def part1(pairs):
    return sum(1 for elf1, elf2 in pairs if elf1 >= elf2 or elf2 >= elf1)


def part2(pairs):
    return sum(1 for elf1, elf2 in pairs if len(elf1 & elf2) > 0)


if __name__ == "__main__":
    pairs = parse_input(test=False)
    # Part 1
    print(part1(pairs))
    # Part 2
    print(part2(pairs))
