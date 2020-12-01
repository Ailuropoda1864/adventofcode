day = 1

###############################
from collections import Counter
from read_input import *

input_string = get_input_string(day)
input_list = list(map(int, input_string.splitlines()))


# Part One
def find_numbers(num_dict, total=2020):
    for i, count in num_dict.items():
        j = total - i
        if (i != j and j in num_dict.keys()) or (i == j and count >= 2):
            return i * j
    else:
        return None


def part1(input_list):
    return find_numbers(Counter(input_list))


# Part Two
def part2(input_list):
    numbers = Counter(input_list)
    temp = numbers.copy()
    for i, i_count in numbers.items():
        temp[i] = i_count - 1
        results = find_numbers(temp, 2020 - i)
        if results is not None:
            return i * results


if __name__ == '__main__':
    print(part1(input_list))
    print(part2(input_list))
