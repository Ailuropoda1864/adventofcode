day = 5

###############################
from read_input import *
from operator import add, mul, lt, eq

input_string = get_input_string(day)
input_tuple = tuple(map(int, input_string.split(',')))

op_map = {1: add, 2: mul, 7: lt, 8: eq}


def get_value(program, parameter, mode):
    # position mode
    if mode == 0:
        return program[parameter]
    # immediate mode
    elif mode == 1:
        return parameter


def parse(opcode):
    opcode = str(opcode).zfill(4)
    return int(opcode[-2:]), int(opcode[-3]), int(opcode[-4])


def run_program(intcode, input_int):
    addr = 0
    while True:
        opcode, par1_mode, par2_mode = parse(intcode[addr])
        if opcode == 99:
            break
        elif opcode in (1, 2, 5, 6, 7, 8):
            par1 = get_value(intcode, intcode[addr + 1], par1_mode)
            par2 = get_value(intcode, intcode[addr + 2], par2_mode)

            if opcode in (1, 2, 7, 8):
                intcode[intcode[addr + 3]] = int(op_map[opcode](par1, par2))
                addr += 4
            elif opcode == 5:
                if par1 != 0:
                    addr = par2
                else:
                    addr += 3
            else:
                if par1 == 0:
                    addr = par2
                else:
                    addr += 3
        elif opcode == 3:
            intcode[intcode[addr + 1]] = input_int
            addr += 2
        elif opcode == 4:
            output = get_value(intcode, intcode[addr + 1], par1_mode)
            addr += 2
        else:
            raise ValueError('opcode {} not recognized'.format(intcode[addr]))
    return output


# Part One
print(run_program(list(input_tuple), 1))

# Part Two
print(run_program(list(input_tuple), 5))
