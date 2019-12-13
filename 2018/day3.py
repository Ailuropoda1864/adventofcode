day = 3

###############################
from read_input import *

input_string = get_input_string(day)
claims = input_string.splitlines()


# Part One
fabric = [[0 for i in range(1000)] for j in range(1000)]

counter = 0
for claim in claims:
    parsed_claim = claim.split(' ')
    inch_to_left, inch_to_top = map(int, parsed_claim[2][:-1].split(','))
    width, height = map(int, parsed_claim[3].split('x'))

    for col in range(inch_to_left, inch_to_left + width):
        for row in range(inch_to_top, inch_to_top + height):
            if fabric[row][col] < 2:
                fabric[row][col] += 1
                if fabric[row][col] == 2:
                    counter += 1

print(counter)


# Part Two
fabric = [['.' for i in range(1000)] for j in range(1000)]

ids = set()
overlap_ids = set()
for claim in claims:
    parsed_claim = claim.split(' ')
    id = parsed_claim[0]
    ids.add(id)

    inch_to_left, inch_to_top = map(int, parsed_claim[2][:-1].split(','))
    width, height = map(int, parsed_claim[3].split('x'))

    for col in range(inch_to_left, inch_to_left + width):
        for row in range(inch_to_top, inch_to_top + height):
            if fabric[row][col] == '.':
                fabric[row][col] = id
            elif fabric[row][col] == 'X':
                overlap_ids.add(id)
            else:
                overlap_ids.add(fabric[row][col])
                overlap_ids.add(id)
                fabric[row][col] = 'X'

print(ids-overlap_ids)


