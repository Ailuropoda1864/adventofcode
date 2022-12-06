DAY = 6

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return input_string


def find_index(line, num_distinct):
    rolling_chars = line[:num_distinct]
    if len(set(rolling_chars)) == num_distinct:
        return num_distinct
    for i in range(num_distinct, len(line)):
        rolling_chars = rolling_chars[1:] + line[i]
        if len(set(rolling_chars)) == num_distinct:
            return i + 1


if __name__ == "__main__":
    line = parse_input(test=False)
    # Part 1
    print(find_index(line, 4))
    # Part 2
    print(find_index(line, 14))
