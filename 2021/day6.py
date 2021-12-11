DAY = 6

###############################
from collections import Counter
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return list(map(int, input_string.split(',')))


def simulate(fishes, days):
    fish_distribution = Counter(fishes)
    for day in range(days):
        new_distribution = Counter({day: 0 for day in range(9)})
        for timer, count in fish_distribution.items():
            if timer - 1 >= 0:
                new_distribution[timer - 1] += count
            else:
                new_distribution[6] += count
                new_distribution[8] += count
        fish_distribution = new_distribution
    return sum(fish_distribution.values())


if __name__ == "__main__":
    # Part 1
    fishes = parse_input(test=False)
    print(simulate(fishes, 80))
    # Part 2
    print(simulate(fishes, 256))


