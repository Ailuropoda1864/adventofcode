day = 19

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
    registers = [0 for _ in range(6)]
    ip = 0
    num_instr = len(instructions)
    while ip < num_instr:
        registers[bound_idx] = ip
        instr = instructions[ip]
        registers = instr[0](registers, *instr[1:])
        ip = registers[bound_idx] + 1
    return registers[0]


def part2(file):
    bound_idx, instructions = parse_input_file(file)
    registers = [1, 0, 0, 0, 0, 0]
    ip = 0
    i = 0
    while i < 20:
        registers[bound_idx] = ip
        instr = instructions[ip]
        registers = instr[0](registers, *instr[1:])
        ip = registers[bound_idx] + 1
        i += 1

    return sum(i for i in range(1, registers[5] + 1) if registers[5] % i == 0)


if __name__ == '__main__':
    file = 'input.txt'

    print(part1(file))
    print(part2(file))
