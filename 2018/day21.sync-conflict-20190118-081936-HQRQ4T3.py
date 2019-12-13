day = 21

###############################
from read_input import *
import re


def addr(before, a, b, c):
    after = before[:]
    after[c] = before[a] + before[b]
    return after


def addi(before, a, b, c):
    after = before[:]
    after[c] = before[a] + b
    return after


def mulr(before, a, b, c):
    after = before[:]
    after[c] = before[a] * before[b]
    return after


def muli(before, a, b, c):
    after = before[:]
    after[c] = before[a] * b
    return after


def banr(before, a, b, c):
    after = before[:]
    after[c] = before[a] & before[b]
    return after


def bani(before, a, b, c):
    after = before[:]
    after[c] = before[a] & b
    return after


def borr(before, a, b, c):
    after = before[:]
    after[c] = before[a] | before[b]
    return after


def bori(before, a, b, c):
    after = before[:]
    after[c] = before[a] | b
    return after


def setr(before, a, b, c):
    after = before[:]
    after[c] = before[a]
    return after


def seti(before, a, b, c):
    after = before[:]
    after[c] = a
    return after


def gtir(before, a, b, c):
    after = before[:]
    after[c] = int(a > before[b])
    return after


def gtri(before, a, b, c):
    after = before[:]
    after[c] = int(before[a] > b)
    return after


def gtrr(before, a, b, c):
    after = before[:]
    after[c] = int(before[a] > before[b])
    return after


def eqir(before, a, b, c):
    after = before[:]
    after[c] = int(a == before[b])
    return after


def eqri(before, a, b, c):
    after = before[:]
    after[c] = int(before[a] == b)
    return after


def eqrr(before, a, b, c):
    after = before[:]
    after[c] = int(before[a] == before[b])
    return after


def parse_input_file(file):
    with open(file) as f:
        bnd_id = int(re.match(r'#ip ([0-9]+)', f.readline()).group(1))
        instr = []
        for line in f.readlines():
            func, a, b, c = line.split()
            instr.append((eval(func), int(a), int(b), int(c)))
    return bnd_id, instr


def part1(file):
    bound_idx, instructions = parse_input_file(file)
    registers = [0, 0, 0, 0, 0, 0]
    ip = 0
    num_instr = len(instructions)
    while ip < num_instr and ip != 28:
        registers[bound_idx] = ip
        instr = instructions[ip]
        registers = instr[0](registers, *instr[1:])
        ip = registers[bound_idx] + 1

    return registers[5]


def part2(file):
    bound_idx, instructions = parse_input_file(file)
    registers = [0, 0, 0, 0, 0, 0]
    ip = 0
    num_instr = len(instructions)
    register5 = []
    while ip < num_instr:
        # print(ip)
        registers[bound_idx] = ip
        # print(registers)
        instr = instructions[ip]
        # print(instr)
        if ip == 28:
            if registers[5] in register5:
                break
            register5.append(registers[5])
            print(register5)
        registers = instr[0](registers, *instr[1:])
        # print(registers)
        # print('\n')
        ip = registers[bound_idx] + 1

    return register5


if __name__ == '__main__':
    file = 'input.txt'

    #print(part1(file))
    print(part2(file))