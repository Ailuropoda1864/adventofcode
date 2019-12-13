import string
from functools import partial


TEST = '/home/fay/Downloads/test.txt'


# pt 1
def spin(programs, x):
    x = int(x)
    return programs[-x:] + programs[: len(programs)-x]


def exchange_partner(programs, x, move):
    a, b = x.split('/')
    a, b = map(int, [a, b]) if move == 'x' \
        else map(lambda char: programs.index(char), [a, b])

    temp = programs[:]
    temp[a] = programs[b]
    temp[b] = programs[a]
    return temp


def parse_file(file):
    funcs = {'s': spin,
             'x': partial(exchange_partner, move='x'),
             'p': partial(exchange_partner, move='p')}

    with open(file) as f:
        return [(funcs[parsed[0]], parsed[1:])
                for parsed in f.readline().strip().split(',')]


def dancing(file, programs=list(string.ascii_lowercase[:16])):
    moves = parse_file(file)

    for func, x in moves:
        programs = func(programs, x)

    return ''.join(programs)


# pt 2
def dancing_rounds(file, n, programs=list(string.ascii_lowercase[:16])):
    moves = parse_file(file)

    seqs = []
    for _ in range(n):
        for func, x in moves:
            programs = func(programs, x)
        output = ''.join(programs)

        if output not in seqs:
            seqs.append(output)
        else:
            cycle = seqs[seqs.index(output):]
            return cycle[(n - len(seqs)) % len(cycle) - 1]


def main():
    print(dancing(TEST))
    print(dancing_rounds(TEST, 10 ** 9))


if __name__ == '__main__':
    main()