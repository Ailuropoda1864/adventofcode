DAY = 10

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return input_string.splitlines()


def part1(input_lines):
    close_to_open_mapping = {")": "(", "]": "[", "}": "{", ">": "<"}
    close_to_point_mapping = {")": 3, "]": 57, "}": 1197, ">": 25137}
    points = 0
    for line in input_lines:
        open_chunks = ""
        for sym in line:
            if sym in close_to_open_mapping.values():
                open_chunks += sym
            else:
                # what's open last must be closed first
                if close_to_open_mapping[sym] != open_chunks[-1]:
                    points += close_to_point_mapping[sym]
                    break
                else:
                    open_chunks = open_chunks[:-1]
    return points


def part2(input_lines):
    close_to_open_mapping = {")": "(", "]": "[", "}": "{", ">": "<"}
    open_to_point_mapping = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in input_lines:
        open_chunks = ""
        for sym in line:
            if sym in close_to_open_mapping.values():
                open_chunks += sym
            else:
                # what's open last must be closed first
                if close_to_open_mapping[sym] != open_chunks[-1]:
                    break
                else:
                    open_chunks = open_chunks[:-1]
        else:
            score = 0
            for sym in open_chunks[-1::-1]:
                score *= 5
                score += open_to_point_mapping[sym]
            scores.append(score)
    assert len(scores) % 2 == 1
    scores.sort()
    return scores[(len(scores) - 1) // 2]


if __name__ == "__main__":
    input_lines = parse_input(test=False)
    # Part 1
    print(part1(input_lines))
    # Part 2
    print(part2(input_lines))
