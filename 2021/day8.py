DAY = 8

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return [line.split(" | ") for line in input_string.splitlines()]


def part1(parsed_input):
    return sum(
        (
            1
            for patterns, outputs in parsed_input
            for digit in outputs.split()
            if len(digit) in (2, 4, 3, 7)
        )
    )


def decipher(patterns: tuple):
    pattern_set = [None for i in range(10)]
    # easy digits: 1, 4, 7, 8
    for p in patterns:
        if len(p) == 2:
            pattern_set[1] = p
        elif len(p) == 4:
            pattern_set[4] = p
        elif len(p) == 3:
            pattern_set[7] = p
        elif len(p) == 7:
            pattern_set[8] = p

    # difference between digit 7 and digit 1 is the top horizontal zone
    horizontal1 = pattern_set[7] - pattern_set[1]
    assert (len(horizontal1)) == 1, "Horizontal 1 is wrong"

    # what digits 2, 3, 4 and 5 have in common is the middle horizontal zone
    horizontal2 = set(pattern_set[4])
    for p in patterns:
        if len(p) == 5:
            horizontal2 &= p
    assert (len(horizontal2)) == 1, "Horizontal 2 is wrong"

    # upper left zone
    left1 = pattern_set[4] - horizontal2 - pattern_set[1]
    assert (len(left1)) == 1, "Left 1 is wrong"

    # out of digits 2, 3, 5
    for p in patterns:
        if len(p) == 5:
            # only digit 3 have two zones in common with digit 1
            if len(p & pattern_set[1]) == 2:
                pattern_set[3] = p
            # only digit 5 have upper left zone
            elif len(p & left1) == 1:
                pattern_set[5] = p
            else:
                pattern_set[2] = p

    horizontal3 = pattern_set[3] - pattern_set[1] - horizontal2 - horizontal1
    assert (len(horizontal3)) == 1, "Horizontal 3 is wrong"

    left2 = pattern_set[2] - pattern_set[3]
    assert (len(left2)) == 1, "Left 2 is wrong"
    right1 = pattern_set[2] & pattern_set[1]
    assert (len(right1)) == 1, "Right 1 is wrong"
    right2 = pattern_set[1] - right1
    assert (len(right2)) == 1, "Right 2 is wrong"

    # fill in digits 0, 6, 9
    pattern_set[0] = pattern_set[7] | left1 | left2 | horizontal3
    pattern_set[9] = pattern_set[7] | left1 | horizontal2 | horizontal3
    pattern_set[6] = pattern_set[5] | left2

    for digit, p in enumerate(pattern_set):
        assert p is not None, f"Digit {digit} pattern is incorrect"

    return pattern_set


def part2(parsed_input):
    total = 0
    for patterns, outputs in parsed_input:
        digit_to_pattern = decipher(tuple(set(p) for p in patterns.split()))
        pattern_to_digit = {
            frozenset(pattern): digit for digit, pattern in enumerate(digit_to_pattern)
        }
        total += int(
            "".join([str(pattern_to_digit[frozenset(o)]) for o in outputs.split()])
        )
    return total


if __name__ == "__main__":
    parsed_input = parse_input(test=False)
    # Part 1
    print(part1(parsed_input))
    # Part 2
    print(part2(parsed_input))
