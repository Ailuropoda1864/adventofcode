day = 1

###############################
from read_input import *

input_string = get_input_string(day)
input_list = list(map(int, input_string.splitlines()))


# Part One
def get_fuel(mass):
    fuel = int(mass / 3) - 2
    if fuel < 0:
        return 0
    return fuel


print(sum([get_fuel(m) for m in input_list]))


# Part Two
def get_total_fuel(mass):
    total_fuel = 0
    new_mass = mass
    while new_mass > 0:
        new_mass = get_fuel(new_mass)
        total_fuel += new_mass
    return total_fuel


print(sum([get_total_fuel(m) for m in input_list]))
