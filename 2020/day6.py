day = 6

###############################
from functools import reduce
from read_input import *

input_string = get_input_string(day)
# input_string = read_file('test.txt')


def count_answer(input_string, set_operation):
    return sum(
        len(
            reduce(
                set_operation,
                map(set, group.split())
            )
        ) for group in input_string.split('\n\n'))


if __name__ == '__main__':
    print(count_answer(input_string, set.union))
    print(count_answer(input_string, set.intersection))
