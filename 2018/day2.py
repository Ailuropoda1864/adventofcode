day = 2

###############################
from read_input import *

input_string = get_input_string(day)
box_ids = input_string.splitlines()


# Part One
from collections import Counter


def checksum(box_ids):
    count_twice = 0
    count_thrice = 0

    for id in box_ids:
        counter = Counter(id)
        count_twice += (2 in counter.values())
        count_thrice += (3 in counter.values())

    return count_twice * count_thrice


print(checksum(box_ids))


# Part Two
from itertools import combinations


def compare_id(id1, id2):
    counter = 0
    for i, char in enumerate(id1):
        if char != id2[i]:
            counter += 1
            if counter > 1:
                return False
    else:
        return counter == 1


def find_common_letters(box_ids):
    for id1, id2 in combinations(box_ids, 2):
        if compare_id(id1, id2):
            return ''.join([char for i, char in enumerate(id1) if char == id2[i]])


print(find_common_letters(box_ids))
