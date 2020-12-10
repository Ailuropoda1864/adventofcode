day = 9

###############################
from itertools import combinations
from read_input import *

input_string = get_input_string(day)
# input_string = read_file('test.txt')

input_list = list(map(int, input_string.splitlines()))

# Part One
def part1(input_list, preamble_len=25):
    idx = preamble_len
    input_length = len(input_list)
    while idx < input_length:
        if validate(input_list[idx - preamble_len: idx], input_list[idx]):
            idx += 1
        else:
            return input_list[idx]


def validate(preamble, number):
    for num1, num2 in combinations(preamble, 2):
        if num1 + num2 == number:
            return True
    return False


# Part Two
def part2(input_list, target):
    first_idx, last_idx = find_contiguous_set(input_list, target)
    final_list = input_list[first_idx: last_idx + 1]
    return min(final_list) + max(final_list)


def find_contiguous_set(input_list, target):
    first_idx = 0
    last_idx = 1
    total = sum(input_list[first_idx: last_idx + 1])
    input_length = len(input_list)
    while last_idx < input_length:
        if total == target:
            return first_idx, last_idx
        elif total < target:
            last_idx += 1
            total += input_list[last_idx]
        else:
            total -= input_list[first_idx]
            first_idx += 1


if __name__ == '__main__':
    invalid_num = part1(input_list, 25)
    print(invalid_num)
    print(part2(input_list, invalid_num))