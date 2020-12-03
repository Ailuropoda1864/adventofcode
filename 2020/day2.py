day = 2

###############################
import re
from read_input import *


input_string = get_input_string(day)
#input_string = read_file('test.txt')

# Part One
def part1(input_string):
    return len([
        password for min_count, max_count, letter, _, password in (
            re.split('\W', row) for row in input_string.splitlines()
        )
        if int(min_count) <= password.count(letter) <= int(max_count)
    ])



# Part Two
def part2(input_string):
    return len([
        password for idx1, idx2, letter, _, password in (
            re.split('\W', row) for row in input_string.splitlines()
        )
        if (password[int(idx1)-1] == letter) != (password[int(idx2)-1] == letter)
    ])


if __name__ == '__main__':
    print(part1(input_string))
    print(part2(input_string))
