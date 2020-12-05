day = 5

###############################
import re
from read_input import *

input_string = get_input_string(day)
# input_string = read_file('test.txt')

input_list = input_string.splitlines()

# Part One
def id_generator(input_list):
    # Getting the seat ID from the boarding pass
    # is essentially converting binary to decimal
    char_map = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}
    return (
        int(''.join([char_map[char] for char in s]), 2)
        for s in input_list
    )


def part1(input_list):
    return max(id_generator(input_list))


# Part Two
def part2(input_list):
    seats = set(range(2**10))
    existing = set(id_generator(input_list))
    return [
        missing for missing in seats - existing
        if {missing + 1, missing - 1} < existing
    ]


if __name__ == '__main__':
    print(part1(input_list))
    print(part2(input_list))
