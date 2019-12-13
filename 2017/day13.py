TEST = '/home/fay/Downloads/test.txt'


def main():
    firewall = parse_file(TEST)
    positions_map = {range_: pos_cycle(range_)
                     for range_ in set(firewall.values())}
    print(cal_severity(firewall, positions_map))
    print(find_delay(firewall, positions_map))


def parse_file(file):
    firewall = {}
    with open(file) as f:
        for line in f:
            layer, range = map(int, line.strip().split(': '))
            firewall[layer] = range
    return firewall


def pos_cycle(range_):
    direction = 1
    positions = [1]
    cycle = range_ * 2 - 3
    for i in range(cycle):
        if i == range_ - 1:
            direction = -1
        positions.append(positions[-1] + direction)
    return positions


def find_scanner(firewall, positions_map, layer, lapse):
    positions = positions_map[firewall[layer]]
    return positions[lapse % len(positions)]


def cal_severity(firewall, position_map):
    severity = 0
    for layer in range(max(firewall.keys()) + 1):
        if layer in firewall.keys() \
                and find_scanner(firewall, position_map, layer, layer) == 1:
            severity += layer * firewall[layer]
    return severity


# pt 2
def is_caught(firewall, position_map, delay):
    for layer in range(max(firewall.keys()) + 1):
        if layer in firewall.keys() and find_scanner(
                firewall, position_map, layer, delay + layer) == 1:
            return True
    return False


def find_delay(firewall, position_map):
    delay = 0
    while is_caught(firewall, position_map, delay):
        delay += 1
    return delay


if __name__ == '__main__':
    main()
