import operator


# pt 1
class Instruction(object):
    def __init__(self, register1, change, register2, cf):
        self.name = register1
        self.change = change
        self.other_name = register2
        self.cf = cf

    def update(self, registers):
        if self.cf(registers[self.other_name]):
            registers[self.name] = self.change(registers[self.name])


def parse_instr(line):
    operators = {'>': operator.gt,
                 '<': operator.lt,
                 '>=': operator.ge,
                 '<=': operator.le,
                 '==': operator.eq,
                 '!=': operator.ne,
                 'inc': operator.add,
                 'dec': operator.sub}

    l = line.split()
    return Instruction(l[0],
                       lambda x: operators[l[1]](x, int(l[2])),
                       l[4],
                       lambda x: operators[l[5]](x, int(l[6])))


def load_file(file):
    with open(file) as f:
        instructions = [parse_instr(line) for line in f]
        register_names = set([instr.name for instr in instructions])
        return instructions, {name: 0 for name in register_names}


def run_inst(instructions, registers):
    for instr in instructions:
        instr.update(registers)
    return max(registers.values())


# pt 2
def run_inst2(instructions, registers):
    max_value = -float('inf')
    for instr in instructions:
        instr.update(registers)
        if registers[instr.name] > max_value:
            max_value = registers[instr.name]
    return max_value
