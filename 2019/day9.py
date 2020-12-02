day = 9

###############################
from operator import add, mul, lt, eq

from read_input import *


input_string = get_input_string(day)
input_tuple = tuple(map(int, input_string.split(',')))


class Amplifier:
    op_map = {1: add, 2: mul, 7: lt, 8: eq}

    def __init__(self, software, input=None):
        self.program = {k: v for k, v in enumerate(software)}
        self.relative_base = 0
        self.output = []
        if input is None:
            self.input_queue = []
        else:
            self.input_queue = [input]

    def run_program(self):
        addr = 0
        while True:
            opcode, par1_mode, par2_mode, par3_mode = self.parse(self.read(addr))
            if opcode == 99:
                break
            elif opcode in (1, 2, 5, 6, 7, 8):
                par1 = self.get_value(self.read(addr + 1), par1_mode)
                par2 = self.get_value(self.read(addr + 2), par2_mode)

                if opcode in (1, 2, 7, 8):
                    self.write(
                        self.read(addr + 3),
                        par3_mode,
                        int(self.op_map[opcode](par1, par2)))
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
                self.write(
                    self.read(addr + 1),
                    par1_mode,
                    self.input_queue.pop(0)
                )
                addr += 2
            elif opcode == 4:
                self.output.append(self.get_value(self.read(addr + 1), par1_mode))
                addr += 2
            elif opcode == 9:
                self.relative_base += self.get_value(self.read(addr + 1), par1_mode)
                addr += 2
            else:
                raise ValueError(f'opcode {opcode} not recognized')

    def get_value(self, parameter, mode):
        # position mode
        if mode == 0:
            return self.read(parameter)
        # immediate mode
        elif mode == 1:
            return parameter
        # relative mode
        elif mode == 2:
            return self.read(parameter + self.relative_base)
        else:
            raise ValueError(f'mode {mode} not recognized')

    def read(self, address):
        assert address >= 0, f'address {address} must be non-negative'
        return self.program.get(address, 0)

    def write(self, address, mode, value):
        if mode == 2:  # relative mode
            address += self.relative_base
        assert address >= 0, f'address {address} must be non-negative'
        self.program[address] = value

    @staticmethod
    def parse(opcode):
        opcode = str(opcode).zfill(5)
        return int(opcode[-2:]), int(opcode[-3]), int(opcode[-4]), int(opcode[-5])


# Part One
def part1(input_tuple):
    boost = Amplifier(input_tuple, 1)
    boost.run_program()
    return boost.output


# Part Two
def part2(input_tuple):
    boost = Amplifier(input_tuple, 2)
    boost.run_program()
    return boost.output


if __name__ == '__main__':
    print(part1(input_tuple))
    print(part2(input_tuple))
