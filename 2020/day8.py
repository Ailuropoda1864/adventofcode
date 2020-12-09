day = 8

###############################
from read_input import *

input_string = get_input_string(day)
# input_string = read_file('test.txt')


class InfiniteLoopError(Exception):
    pass


class BootCode:
    def __init__(self, boot_code):
        self.instructions = [instr.split() for instr in boot_code.splitlines()]

    def run(self):
        num_instr = len(self.instructions)
        instr_idx = 0
        accumulator = 0
        executed_instr = set()
        try:
            while instr_idx < num_instr:
                operation, argument = self.instructions[instr_idx]
                executed_instr.add(instr_idx)
                if operation == 'acc':
                    accumulator += int(argument)
                    instr_idx += 1
                elif operation == 'jmp':
                    instr_idx += int(argument)
                elif operation == 'nop':
                    instr_idx += 1
                else:
                    raise ValueError(f"Operation {operation} not recognized")
                if instr_idx in executed_instr:
                    raise InfiniteLoopError
        except InfiniteLoopError:
            return False, accumulator
        return True, accumulator

    def debug(self):
        for idx in range(len(self.instructions)):
            self.flip_instruction(idx)
            success, accumulator = self.run()
            if success:
                return accumulator
            self.flip_instruction(idx)

    def flip_instruction(self, idx):
        op = self.instructions[idx][0]
        if op == 'jmp':
            self.instructions[idx][0] = 'nop'
        elif op == 'nop':
            self.instructions[idx][0] = 'jmp'


def part1(boot_code):
    success, accumulator = boot_code.run()
    assert success is False
    return accumulator


def part2(boot_code):
    return boot_code.debug()


if __name__ == '__main__':
    boot_code = BootCode(input_string)
    print(part1(boot_code))
    print(part2(boot_code))
