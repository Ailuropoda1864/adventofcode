day = 2

###############################
from read_input import *


input_string = get_input_string(day)
#input_string = read_file('test.txt')

# Part One
def part1(input_string):
    valid_count = 0
    for row in input_string.splitlines():
        policy, password = row.split(': ')
        count_range, letter = policy.split(' ')
        min_count, max_count = list(map(int, count_range.split('-')))
        if min_count <= password.count(letter) <= max_count:
            valid_count += 1
    return valid_count


# Part Two
def part2(input_string):
    valid_count = 0
    for row in input_string.splitlines():
        policy, password = row.split(': ')
        indices, letter = policy.split(' ')
        idx1, idx2 = list(map(int, indices.split('-')))
        if (password[idx1-1] == letter) != (password[idx2-1] == letter):
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    print(part1(input_string))
    print(part2(input_string))
