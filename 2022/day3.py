DAY = 3

###############################
import string

from read_input import *

ITEM_TYPE_TO_PRIORITY = {
    **{char: 1 + ord(char) - ord("a") for char in string.ascii_lowercase},
    **{char: 27 + ord(char) - ord("A") for char in string.ascii_uppercase},
}


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return input_string.splitlines()


def get_common_item_type_part1(line):
    assert (
        len(line) % 2 == 0
    ), f"The number of characters in '{line}' is: {len(line)}, which is not an even number"
    midpoint = int(len(line) / 2)
    comp1 = line[:midpoint]
    comp2 = line[midpoint:]
    common_item_type = set(comp1) & set(comp2)
    assert len(common_item_type) == 1
    return common_item_type.pop()


def part1(lines):
    return sum(
        ITEM_TYPE_TO_PRIORITY[get_common_item_type_part1(line)] for line in lines
    )


def get_common_item_type_part2(group):
    common_item_type = set(group[0]) & set(group[1]) & set(group[2])
    assert len(common_item_type) == 1
    return common_item_type.pop()


def part2(lines):
    assert len(lines) % 3 == 0
    return sum(
        ITEM_TYPE_TO_PRIORITY[get_common_item_type_part2(lines[i : i + 3])]
        for i in range(0, len(lines), 3)
    )


if __name__ == "__main__":
    input_lines = parse_input(test=False)
    # Part 1
    print(part1(input_lines))
    # Part 2
    print(part2(input_lines))
