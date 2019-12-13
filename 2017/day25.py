STATES = {
    'A': ((1, 1, 'B'), (0, -1, 'D')),
    'B': ((1, 1, 'C'), (0, 1, 'F')),
    'C': ((1, -1, 'C'), (1, -1, 'A')),
    'D': ((0, -1, 'E'), (1, 1, 'A')),
    'E': ((1, -1, 'A'), (0, 1, 'B')),
    'F': ((0, 1, 'C'), (0, 1, 'E'))
}


def diagnosis(init_state, num_steps):
    tape = {0: 0}
    position = 0
    state = init_state
    for _ in range(num_steps):
        if position not in tape.keys():
            tape[position] = 0
        value, direction, state = STATES[state][tape[position]]
        tape[position] = value
        position += direction

    return sum(tape.values())


def main():
    print(diagnosis('A', 12317297))


if __name__ == '__main__':
    main()
