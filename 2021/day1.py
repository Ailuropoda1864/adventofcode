DAY = 1

###############################
from read_input import *


def parse_input(test=True):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return list(map(int, input_string.splitlines()))


def count_increase(lst, window_len=1):
    count = 0
    for i in range(len(lst) - window_len):
        if sum(lst[i : i + window_len]) < sum(lst[i + 1 : i + 1 + window_len]):
            count += 1
    return count


if __name__ == "__main__":
    input_list = parse_input(test=False)
    # Part 1
    print(count_increase(input_list))
    # Part 2
    print(count_increase(input_list, 3))
