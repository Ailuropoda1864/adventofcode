day = 7

###############################
from read_input import *
from operator import add, mul, lt, eq

input_string = get_input_string(day)
#input_string = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
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


def run_program(intcode, inputs):
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
            intcode[intcode[addr + 1]] = inputs.pop(0)
            addr += 2
        elif opcode == 4:
            output = get_value(intcode, intcode[addr + 1], par1_mode)
            addr += 2
        else:
            raise ValueError('opcode {} not recognized'.format(intcode[addr]))
    return output


# Part One
def get_settings(start, end):
    seqs = []
    choices = range(start, end + 1)
    for a in choices:
        for b in choices:
            for c in choices:
                for d in choices:
                    for e in choices:
                        if len({a, b, c, d, e}) == 5:
                            seqs.append((a, b, c, d, e))
    return seqs


def part1():
    max_output = None
    settings = get_settings(0, 4)
    for s in settings:
        # Amp A
        output_a = run_program(list(input_tuple), [s[0], 0])
        # Amp B
        output_b = run_program(list(input_tuple), [s[1], output_a])
        # Amp C
        output_c = run_program(list(input_tuple), [s[2], output_b])
        # Amp D
        output_d = run_program(list(input_tuple), [s[3], output_c])
        # Amp E
        output_e = run_program(list(input_tuple), [s[4], output_d])

        if max_output is None or max_output < output_e:
            max_output = output_e

    return max_output


print(part1())


# Part Two




