DAY = 14

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    insert_mapping = {}
    for line in input_string.splitlines():
        line = line.strip()
        if line == "":
            continue
        elif "->" in line:
            pair, insert_element = line.split(" -> ")
            insert_mapping[pair] = insert_element
        else:
            template = line
    return template, insert_mapping


def insert_one_time(pair_counts):
    new_pair_counts = {}
    for pair, count in pair_counts.items():
        insert_element = INSERT_MAPPING[pair]
        pair1 = pair[0] + insert_element
        pair2 = insert_element + pair[1]
        new_pair_counts[pair1] = new_pair_counts.get(pair1, 0) + count
        new_pair_counts[pair2] = new_pair_counts.get(pair2, 0) + count
    return new_pair_counts


def polymerize(template, steps):
    pair_counts = {}
    for i in range(len(template) - 1):
        pair_counts[template[i : i + 2]] = pair_counts.get(template[i : i + 2], 0) + 1
    for _ in range(steps):
        pair_counts = insert_one_time(pair_counts)
    counts = {}
    for pair, count in pair_counts.items():
        counts[pair[0]] = counts.get(pair[0], 0) + count
    counts[template[-1]] = counts.get(template[-1], 0) + 1
    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    TEMPLATE, INSERT_MAPPING = parse_input(test=False)

    # Part 1
    print(polymerize(TEMPLATE, 10))
    # Part 2
    print(polymerize(TEMPLATE, 40))
