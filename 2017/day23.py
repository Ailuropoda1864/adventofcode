import operator


TEST = '/home/fay/Downloads/test.txt'


# pt 1
FUNCS = {
    'set': lambda x, y: y,
    'sub': operator.sub,
    'mul': operator.mul
}


def parse_instructions(file):
    with open(file) as f:
        return [line.split() for line in f]


def find_value(value, registers):
    return registers[value] if value in registers.keys() else int(value)


def run_instructions(instructions):
    registers = {letter: 0 for letter in 'abcdefgh'}
    i = 0
    count = 0

    while 0 <= i < len(instructions):
        instr = instructions[i]
        method, value1, value2 = instr

        y = find_value(value2, registers)

        if method == 'jnz':
            x = find_value(value1, registers)
            if x != 0:
                i += y
                continue
        else:
            registers[value1] = FUNCS[method](registers[value1], y)
            if method == 'mul':
                count += 1

        i += 1

    return count


# pt 2
# def run_instructions2(instructions):
#     registers = {letter: 0 for letter in 'bcdefgh'}
#     registers['a'] = 1
#     i = 0
#
#     while 0 <= i < len(instructions):
#         instr = instructions[i]
#         method, value1, value2 = instr
#
#         y = find_value(value2, registers)
#
#         if method == 'jnz':
#             x = find_value(value1, registers)
#             if x != 0:
#                 i += y
#                 continue
#         else:
#             registers[value1] = FUNCS[method](registers[value1], y)
#             if value1 == 'a':
#                 return registers['h']
#
#         i += 1
#
# #    return registers['h']
def prime_generator():
    primes = [2, 3]
    for prime in primes:
        yield prime

    n = 5
    while True:
        for prime in primes:
            if n % prime == 0:
                n += 2
                break
        else:
            primes.append(n)
            yield n








def main():
    # part 1
    instructions = parse_instructions(TEST)
    print(run_instructions(instructions))

    # part 2
    b = 99 * 100 + 100000
    c = b + 17000

    p_gen = prime_generator()
    number = next(p_gen)
    primes = set()
    while number <= c:
        number = next(p_gen)
        primes.add(number)

    count = 0
    for i in range(b, c + 1, 17):
        if i not in primes:
            count += 1

    print(count)



if __name__ == '__main__':
    main()

