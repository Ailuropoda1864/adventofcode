DAY = 3

###############################
from read_input import *


def parse_input(test=True):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return input_string.splitlines()


def count_bit(report, bit_position):
    return sum((1 for line in report if line[bit_position] == "1"))


def part1(report):
    gamma = ""
    epsilon = ""
    for i in range(len(report[0])):
        if count_bit(report, i) > len(report) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def filter_report(report, bit_position, keep_most_common_value):
    count = count_bit(report, bit_position)
    if (count >= len(report) / 2) == keep_most_common_value:
        return [line for line in report if line[bit_position] == "1"]
    else:
        return [line for line in report if line[bit_position] != "1"]


def get_rating(report, keep_most_common_value):
    for i in range(len(report[0])):
        report = filter_report(report, i, keep_most_common_value)
        if len(report) == 1:
            return report[0]


def part2(report):
    oxygen_generator_rating = get_rating(report, True)
    co2_scrubber_rating = get_rating(report, False)
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":
    input_list = parse_input(test=False)
    # Part 1
    print(part1(input_list))
    # Part 2
    print(part2(input_list))
