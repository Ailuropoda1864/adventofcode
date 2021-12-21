DAY = 15

###############################
from read_input import *



def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return {
        (x, y): int(risk)
        for y, line in enumerate(input_string.splitlines())
        for x, risk in enumerate(line)
    }


def get_neighbors(node):
    x, y = node
    return [
        c
        for c in [(x + 1, y), (x, y + 1)]
        if c in CAVE_MAP.keys()
    ]


def get_greedy_baseline():
    """Each step, we can only traverse right or down, whichever has a lower risk"""
    node = (0, 0)
    path = [(0, 0)]
    while node != (X_MAX, Y_MAX):
        x, y = node
        if x + 1 > X_MAX:
            node = (x, y + 1)
        elif y + 1 > Y_MAX:
            node = (x + 1, y)
        elif CAVE_MAP[(x + 1, y)] > CAVE_MAP[(x, y + 1)]:
            node = (x, y + 1)
        else:
            node = (x + 1, y)
        path.append(node)
    return sum_risk(path)


def sum_risk(nodes):
    return sum((CAVE_MAP[c] for c in nodes)) - CAVE_MAP[(0, 0)]


def validate(node, visited):
    if node in visited:
        return False
    x, y = node
    return sum_risk(visited + [node]) + (Y_MAX - y) + (X_MAX - x) < risk_baseline


def traverse(start, end, visited, paths):
    global risk_baseline
    for node in get_neighbors(start):
        if node == end:
            visited.append(node)
            paths.append(visited[:])
            total_risk = sum_risk(visited)
            if total_risk < risk_baseline:
                risk_baseline = total_risk
            print(f'New path added: {visited}')
            print(f'Total risk: {total_risk}')
            print(f'Current number of paths: {len(paths)}')
            print('-' * 30)
            visited.pop()
        elif validate(node, visited):
            visited.append(node)
            traverse(node, end, visited, paths)
    visited.pop()


def part1():
    global risk_baseline
    risk_baseline = get_greedy_baseline()
    print(f'Baseline: {risk_baseline}')
    paths = []
    traverse((0, 0), (X_MAX, Y_MAX), [(0, 0)], paths)
    print(f'Number of paths considered: {len(paths)}')
    if len(paths) == 0:
        return risk_baseline
    min_risk = risk_baseline
    for path in paths:
        risk = sum_risk(path)
        if risk < min_risk:
            min_risk = risk
    return min_risk


def part2():
    pass


if __name__ == "__main__":
    CAVE_MAP = parse_input(test=True)
    X_MAX = max([x for x, _ in CAVE_MAP.keys()])
    Y_MAX = max([y for _, y in CAVE_MAP.keys()])
    # Part 1
    print(f'lowest risk: {part1()}')
    # Part 2
    # print(part2())
