DAY = 7

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return list(map(int, input_string.split(',')))


def find_least_fuel(positions, fuel_func):
    least_fuel = sys.maxsize
    min_p = min(positions)
    max_p = max(positions)
    for p in range(min_p, max_p + 1):
        fuel = sum((fuel_func(p - p2) for p2 in positions))
        if fuel < least_fuel:
            least_fuel = fuel
    return least_fuel


def cumulative_sum(n):
    n = abs(n)
    return int((1 + n) * n / 2)


if __name__ == "__main__":
    positions = parse_input(test=False)
    # Part 1
    print(find_least_fuel(positions, abs))
    # Part 2
    print(find_least_fuel(positions, cumulative_sum))



