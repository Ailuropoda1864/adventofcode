day = 5

###############################
from read_input import *

input_string = get_input_string(day)


# Part One
def is_react(unit1, unit2):
    return abs(ord(unit1) - ord(unit2)) == 32


def check_remaining(remaining):
    return remaining[1:] if len(remaining) > 1 else ''


def polymerize(remaining, accumulated=''):
    while remaining:
        if not accumulated:
            accumulated = remaining[0]
            remaining = remaining[1:]
        elif is_react(accumulated[-1], remaining[0]):
            accumulated = accumulated[:-1]
            remaining = check_remaining(remaining)
        else:
            accumulated = accumulated + remaining[0]
            remaining = check_remaining(remaining)
    return accumulated


print(len(polymerize(input_string)))


# Part Two
def find_faulty_unit(string):
    return min(len(polymerize(''.join(
        [letter for letter in string
         if letter.lower() != faulty_unit])
    )) for faulty_unit in set(string.lower()))


print(find_faulty_unit(input_string))



##### Jeff
from functools import reduce
magic_number = ord('a') - ord('A')


def reaction(acc, char):
    if not acc:
        return char
    elif abs(ord(acc[-1]) - ord(char)) == magic_number:
        return acc[:-1]
    else:
        return acc + char


def part1():
    return len(reduce(reaction, input_string))


def find_shortest(polymer):
    polymer_components = set(polymer.lower())
    polymer_variations = [polymer.replace(c, '').replace(c.upper(), '')
                          for c in polymer_components]
    return min(len(reduce(reaction, p)) for p in polymer_variations)


def part2():
    return find_shortest(input_string)


print(part1())
print(part2())

