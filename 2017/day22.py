TEST = '/home/fay/Downloads/test.txt'


# pt 1
def read_map(file):
    input_map = {}
    with open(file) as f:
        for i, line in enumerate(f):
            for j, status in enumerate(line.strip()):
                input_map[(i, j)] = status
                ncol = j + 1
            nrow = i + 1
    return input_map, nrow, ncol


def update_position(position, direction):
    i, j = position
    change_in_col, increment = direction
    if change_in_col:
        j += increment
    else:
        i += increment
    return i, j


def infection(input_map, nrow, ncol, n_bursts):
    position = (nrow // 2, ncol // 2)

    # directions: up -> right -> down -> left;
    # first element of inner tuples: 0 - change in row, 1 - change in column
    # second element of inner tuples: increment on the current coordinate
    directions = ((0, -1), (1, 1), (0, 1), (1, -1))

    # begins facing up
    index = 0

    count = 0

    for _ in range(n_bursts):
        # any node not on the original map is not currently infected
        if position not in input_map.keys():
            input_map[position] = '.'

        # burst steps 1 & 2
        if input_map[position] == '.':
            index = (index - 1) % len(directions)
            input_map[position] = '#'
            count += 1
        else:
            index = (index + 1) % len(directions)
            input_map[position] = '.'

        # burst step 3
        position = update_position(position, directions[index])

    return count


# pt 2
def infection2(input_map, nrow, ncol, n_bursts):
    position = (nrow // 2, ncol // 2)

    # directions: up -> right -> down -> left;
    # first element of inner tuples: 0 - change in row, 1 - change in column
    # second element of inner tuples: increment on the current coordinate
    directions = ((0, -1), (1, 1), (0, 1), (1, -1))

    # begins facing up
    index = 0

    count = 0

    for _ in range(n_bursts):
        # any node not on the original map is not currently infected
        if position not in input_map.keys():
            input_map[position] = '.'

        # burst steps 1 & 2
        if input_map[position] == '.':
            index = (index - 1) % len(directions)
            input_map[position] = 'W'
        elif input_map[position] == 'W':
            input_map[position] = '#'
            count += 1
        elif input_map[position] == '#':
            index = (index + 1) % len(directions)
            input_map[position] = 'F'
        else:
            index = (index + 2) % len(directions)
            input_map[position] = '.'

        # burst step 3
        position = update_position(position, directions[index])

    return count


# for debugging
def print_map(input_map):
    i_s, j_s = [], []
    for i, j in input_map.keys():
        i_s.append(i)
        j_s.append(j)
    min_i, min_j = map(min, [i_s, j_s])
    max_i, max_j = map(max, [i_s, j_s])
    nrow = max_i - min_i + 1
    ncol = max_j - min_j + 1

    for row in range(nrow):
        output = ''
        for col in range(ncol):
            output += input_map.get((row + min_i, col + min_j), '.')
        print(output)


def main():
    # part 1
    input_map, nrow, ncol = read_map(TEST)
    print(infection(input_map, nrow, ncol, 10000))

    # part 2
    input_map, nrow, ncol = read_map(TEST)
    print(infection2(input_map, nrow, ncol, 10000000))


if __name__ == '__main__':
    main()
