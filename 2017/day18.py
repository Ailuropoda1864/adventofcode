import operator


TEST = '/home/fay/Downloads/test.txt'


# pt 1
FUNCS = {
    'set': lambda x, y: y,
    'add': operator.add,
    'mul': operator.mul,
    'mod': operator.mod
}


def parse_instructions(file):
    with open(file) as f:
        return [line.split() for line in f]


def run_instructions(instructions):
    registers = {}
    i = 0
    freq = None

    while 0 <= i < len(instructions):
        instr = instructions[i]
        method, name, *value = instr

        try:
            register = int(name)
        except ValueError:
            if name not in registers.keys():
                registers[name] = 0
            register = registers[name]

        if value:
            try:
                value = int(value[0])
            except ValueError:
                value = registers.get(value[0], 0)

        if method == 'snd':
            freq = register
        elif method == 'rcv':
            if register != 0:
                return freq
        elif method == 'jgz':
            if register > 0:
                i += value
                continue
        else:
            registers[name] = FUNCS[method](register, value)

        i += 1


# pt 2
class Program(object):
    def __init__(self, instructions, p):
        self.instructions = instructions
        self.registers = {'p': p}
        self.index = 0
        self.queue = []
        self.sent = 0

    def generator(self, other):
        while 0 <= self.index < len(self.instructions):
            instr = self.instructions[self.index]
            method, name, *value = instr

            try:
                register = int(name)
            except ValueError:
                if name not in self.registers.keys():
                    self.registers[name] = 0
                register = self.registers[name]

            if value:
                try:
                    value = int(value[0])
                except ValueError:
                    value = self.registers.get(value[0], 0)

            if method == 'rcv':
                try:
                    self.registers[name] = other.queue.pop(0)
                except IndexError:
                    yield
                    continue
            elif method == 'snd':
                self.queue.append(register)
                self.sent += 1
            elif method == 'jgz':
                if register > 0:
                    self.index += value
                    continue
            else:
                self.registers[name] = FUNCS[method](register, value)

            self.index += 1


def run_instructions2(instructions):
    program0, program1 = Program(instructions, 0), Program(instructions, 1)
    gen0, gen1 = program0.generator(program1), program1.generator(program0)

    next(gen0)
    next(gen1)

    while True:
        while program0.queue:
            next(gen1)
        while program1.queue:
            next(gen0)
        if len(program0.queue) + len(program1.queue) == 0:
            return program1.sent


def main():
    instructions = parse_instructions(TEST)
    freq = run_instructions(instructions)
    print(freq)

    # pt 2
    count = run_instructions2(instructions)
    print(count)


if __name__ == '__main__':
    main()
