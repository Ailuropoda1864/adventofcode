day = 2

###############################
from read_input import *

input_string = get_input_string(day)
input_tuple = tuple(map(int, input_string.split(',')))


# Part One
def run_program(intcode):
    addr = 0
    while intcode[addr] != 99:
        if intcode[addr] == 1:
            intcode[intcode[addr + 3]] = intcode[intcode[addr + 1]] + intcode[intcode[addr + 2]]
        elif intcode[addr] == 2:
            intcode[intcode[addr + 3]] = intcode[intcode[addr + 1]] * intcode[intcode[addr + 2]]
        else:
            raise ValueError('opcode {} not recognized'.format(intcode[addr]))
        addr += 4
    return intcode


def part1(intcode):
    intcode[1] = 12
    intcode[2] = 2
    return run_program(intcode)[0]


print(part1(list(input_tuple)))


# Part Two
def part2(intcode, output):
    for noun in range(100):
        for verb in range(100):
            temp_intcode = intcode[:]
            temp_intcode[1] = noun
            temp_intcode[2] = verb
            if run_program(temp_intcode)[0] == output:
                return 100 * noun + verb


print(part2(list(input_tuple), 19690720))


