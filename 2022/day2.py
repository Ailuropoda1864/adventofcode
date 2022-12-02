DAY = 2

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return [line.split(" ") for line in input_string.splitlines()]


def calculate_my_score(opponent, me):
    delta = opponent - me
    # draw
    if delta == 0:
        return me + 3
    # opponent defeats me
    elif delta in (1, -2):
        return me
    # I defeat opponent
    else:
        return me + 6


def get_score_part1(round):
    symbol_to_score = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3,  # Scissors
        "X": 1,  # Rock
        "Y": 2,  # Paper
        "Z": 3,  # Scissors
    }
    return calculate_my_score(symbol_to_score[round[0]], symbol_to_score[round[1]])


def get_score_part2(round):
    symbol_to_score = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3,  # Scissors
    }
    opponent_symbol, outcome = round[0], round[1]
    opponent = symbol_to_score[opponent_symbol]
    # lose
    if outcome == "X":
        me = opponent - 1
    # draw:
    elif outcome == "Y":
        me = opponent
    # win
    elif outcome == "Z":
        me = opponent + 1
    else:
        raise Exception(f'Outcome "{outcome}" is not recognized')

    if me == 0:
        me += 3
    elif me == 4:
        me -= 3

    return calculate_my_score(opponent, me)


def get_my_total_score(input_list, score_func):
    return sum(score_func(round) for round in input_list)


if __name__ == "__main__":
    input_list = parse_input(test=False)
    # Part 1
    print(get_my_total_score(input_list, get_score_part1))
    # Part 2
    print(get_my_total_score(input_list, get_score_part2))
