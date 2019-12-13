day = 12

###############################
from read_input import *
import re

input_string = get_input_string(day)


def parse_input(input_string):
    split_input = input_string.splitlines()
    init_state = re.match(r'initial state: ([#.]+)', split_input[0]).group(1)
    pots = {i: char for i, char in enumerate(init_state)}

    notes = {}
    for row in split_input[2:]:
        k, v = re.match(r'([#.]+) => ([#.]+)', row).groups()
        notes[k] = v

    return pots, notes


def get_next_status(pots, notes, pot_position):
    key = ''.join([pots[i] if i in pots.keys() else '.'
                   for i in range(pot_position-2, pot_position+3)])
    return notes[key]


def get_plant_range(pots):
    p = [position for position, pot in pots.items() if pot == '#']
    return min(p), max(p)


def add_empty_pots(pots, id_range):
    for i in id_range:
        if i not in pots.keys():
            pots[i] = '.'


def fill_ends(pots, min_plant, max_plant):
    add_empty_pots(pots, range(min_plant-4, min_plant))
    add_empty_pots(pots, range(max_plant+1, max_plant+5))


def get_sum(pots):
    return sum(id for id, pot in pots.items() if pot == '#')


def is_same_pattern(pots1, pots2):
    pots1 = ''.join([pots1[key] for key in sorted(pots1.keys())]).strip('.')
    pots2 = ''.join([pots2[key] for key in sorted(pots2.keys())]).strip('.')
    return pots1 == pots2


def generation(pots, notes, n_iter=20):
    i=0
    while i < n_iter:
        min_plant, max_plant = get_plant_range(pots)
        fill_ends(pots, min_plant, max_plant)
        temp_pots = {id: get_next_status(pots, notes, id) for id, pot in pots.items()}
        if is_same_pattern(pots, temp_pots):
            break
        pots = temp_pots.copy()
        i += 1

    pot_sum = get_sum(pots)
    diff = get_sum(temp_pots) - pot_sum

    return pot_sum + (n_iter - i) * diff


if __name__ == '__main__':
    pots, notes = parse_input(input_string)

    # Part One
    print(generation(pots, notes))
    # Part Two
    print(generation(pots, notes, 50000000000))
