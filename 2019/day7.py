day = 7

###############################
from read_input import *
from operator import add, mul, lt, eq

input_string = get_input_string(day)
input_tuple = tuple(map(int, input_string.split(',')))


class Amplifier:
    op_map = {1: add, 2: mul, 7: lt, 8: eq}

    def __init__(self, software, phase_setting):
        self.program = list(software)
        self.input_queue = [phase_setting]
        self.generator = self.run_program()

    def run_program(self):
        addr = 0
        while True:
            opcode, par1_mode, par2_mode = self.parse(self.program[addr])
            if opcode == 99:
                break
            elif opcode in (1, 2, 5, 6, 7, 8):
                par1 = self.get_value(self.program[addr + 1], par1_mode)
                par2 = self.get_value(self.program[addr + 2], par2_mode)

                if opcode in (1, 2, 7, 8):
                    self.program[self.program[addr + 3]] = int(self.op_map[opcode](par1, par2))
                    addr += 4
                elif opcode == 5:
                    if par1 != 0:
                        addr = par2
                    else:
                        addr += 3
                else:  # opcode == 6
                    if par1 == 0:
                        addr = par2
                    else:
                        addr += 3
            elif opcode == 3:
                self.program[self.program[addr + 1]] = self.input_queue.pop(0)
                addr += 2
            elif opcode == 4:
                yield self.get_value(self.program[addr + 1], par1_mode)
                addr += 2
            else:
                raise ValueError('opcode %s not recognized' % self.program[addr])

    def get_value(self, parameter, mode):
        # position mode
        if mode == 0:
            return self.program[parameter]
        # immediate mode
        elif mode == 1:
            return parameter

    def add_input(self, input_signal):
        self.input_queue.append(input_signal)

    @staticmethod
    def parse(opcode):
        opcode = str(opcode).zfill(4)
        return int(opcode[-2:]), int(opcode[-3]), int(opcode[-4])


def get_setting_combinations(start, end):
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


# Part One
def part1():
    max_output = float("-inf")
    combos = get_setting_combinations(0, 4)

    for c in combos:
        signal = 0
        for setting in c:
            amp = Amplifier(input_tuple, setting)
            amp.add_input(signal)
            signal = next(amp.generator)
        if max_output < signal:
            max_output = signal

    return max_output


print(part1())


# Part Two
def part2():
    max_output = float("-inf")
    combos = get_setting_combinations(5, 9)

    for c in combos:
        signal = 0
        amps = [Amplifier(input_tuple, setting) for setting in c]

        while True:
            try:
                for idx, amp in enumerate(amps):
                    amp.add_input(signal)
                    signal = next(amp.generator)
            except StopIteration:
                break

        if max_output < signal:
            max_output = signal

    return max_output


print(part2())



