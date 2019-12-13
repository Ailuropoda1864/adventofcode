day = 16

###############################
from read_input import *
import re

input_string = get_input_string(day)


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


FUNCS = (addr, addi, mulr, muli, banr, bani, borr, bori,
         setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr)


def get_possible_opcodes(before, instr, after):
    return {f for f in FUNCS if f(before, *instr[1:]) == after}


def parse_sample(input_string):
    pattern = re.compile(r'Before: \[([0-9 ,]+)]\n([0-9 ]+)\nAfter:  \[([0-9 ,]+)]')
    matches = pattern.findall(input_string)
    return [[list(map(int, m[0].split(', '))),
                list(map(int, m[1].split())),
                list(map(int, m[2].split(', ')))]
            for m in matches]


def part1(samples):
    return sum(len(get_possible_opcodes(*s)) >= 3 for s in samples)


def remove_assigned_opcodes(opcodes, possible_opcodes):
    return possible_opcodes - set(op for op in opcodes if op is not None)


def assign_opcodes(samples):
    opcodes = [None for f in FUNCS]
    possible_opcodes = [[s[1][0], get_possible_opcodes(*s)] for s in samples]
    while None in opcodes:
        for idx, (opcode_idx, p_op) in enumerate(possible_opcodes):
            p_op = remove_assigned_opcodes(opcodes, p_op)
            possible_opcodes[idx][1] = p_op
            if len(p_op) == 1:
                opcodes[opcode_idx] = p_op.pop()
    return opcodes


def parse_test_program(file):
    test = get_input_string_from_file(file).splitlines()
    return [list(map(int, line.split())) for line in test]


def part2(opcodes, test):
    result = [0, 0, 0, 0]
    for t in test:
        func = opcodes[t[0]]
        result = func(result, *t[1:])
    return result[0]


if __name__ == '__main__':
    samples = parse_sample(input_string)

    # Part One
    print(part1(samples))

    # Part Two
    opcodes = assign_opcodes(samples)
    test = parse_test_program('input.txt')
    print(part2(opcodes, test))
