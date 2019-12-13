TEST = '/home/fay/Downloads/test.txt'


def parse_rules(file):
    rules = {}
    with open(file) as f:
        for line in f:
            i_pattern, o_pattern = line.strip().split(' => ')
            rules[i_pattern] = o_pattern
    return rules


parser = lambda string: string.split('/')


joiner = lambda lst: '/'.join(lst)


def vertical_flip(pattern):
    return joiner([p[::-1] for p in parser(pattern)])


def horizontal_flip(pattern):
    return joiner([p for p in parser(pattern)[::-1]])


def rotate_90cw(pattern):
    pattern = parser(pattern)
    new_pattern = [''.join([pattern[i][j]
                            for i in range(len(pattern)-1, -1, -1)])
                   for j in range(len(pattern))]
    return joiner(new_pattern)


def pattern_generator(pattern):
    patterns = [pattern]
    index = 0
    while index < len(patterns):
        pattern = patterns[index]

        new_pattern = vertical_flip(pattern)
        if new_pattern not in patterns:
            patterns.append(new_pattern)
            yield new_pattern

        new_pattern = horizontal_flip(pattern)
        if new_pattern not in patterns:
            patterns.append(new_pattern)
            yield new_pattern

        for _ in range(3):
            new_pattern = rotate_90cw(pattern)
            if new_pattern not in patterns:
                patterns.append(new_pattern)
                yield new_pattern

        index += 1


def enhance(rules, n_iter=5):
    square = parser('.#./..#/###')
    for _ in range(n_iter):
        square = enhance_helper(rules, square, 2) \
            if len(square) % 2 == 0 else enhance_helper(rules, square, 3)
    return joiner(square).count('#')


def enhance_helper(rules, square, divider):
    squares = []
    size = len(square)
    for i in range(0, size, divider):
        for j in range(0, size, divider):
            sub_square = joiner(
                [square[i + n][j:j + divider] for n in range(divider)]
            )
            pattern = pattern_generator(sub_square)
            while sub_square not in rules.keys():
                sub_square = next(pattern)
            squares.append(rules[sub_square])

    new_square = []
    num_sq_per_row = int(len(squares) ** 0.5)
    for i in range(0, len(squares), num_sq_per_row):
        row = [parser(s) for s in squares[i: i + num_sq_per_row]]
        new_square += [''.join([s[j] for s in row]) for j in range(len(row[0]))]
    return new_square


def main():
    # part 1
    rules = parse_rules(TEST)
    print(enhance(rules, 5))

    # part 2
    print(enhance(rules, 18))


if __name__ == '__main__':
    main()
