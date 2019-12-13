day = 9

###############################
from read_input import *
import re
from collections import deque

input_string = get_input_string(day)

n_player, n_marble = map(int, re.match(
    r'([0-9]+) players; last marble is worth ([0-9]+) points', input_string).groups())


def play_faster_game(n_player, n_marble):
    scores = deque([0 for _ in range(n_player)])
    marbles = iter(range(2, n_marble + 1))
    cycle = deque([0, 1])

    for marble in marbles:
        if marble % 23:
            cycle.rotate(2)
            cycle.append(marble)
        else:
            cycle.rotate(-7)
            scores[0] += marble + cycle.pop()

        scores.rotate(1)

    return max(scores)


if __name__ =='__main__':
    # Part One
    print(play_faster_game(n_player, n_marble))

    # Part Two
    print(play_faster_game(n_player, n_marble * 100))


########### Discarded work #############
import itertools

def play_game_in_batch(n_player, n_marble):
    scores = [0 for _ in range(n_player)]

    cycle = [0, 1]
    current_position = 1
    next_marble = 2
    current_to_remove = 23

    while current_to_remove <= n_marble:
        cycle_len = len(cycle)
        insert_position = (current_position + 1) % cycle_len
        num_to_end = cycle_len - insert_position
        num_to_remove = current_to_remove - next_marble
        if num_to_end < num_to_remove:
            num_in_batch = num_to_end
            cycle = cycle[:insert_position] + list(itertools.chain(
                *zip(cycle[insert_position:], range(next_marble, next_marble + num_in_batch + 1))))
            current_position = len(cycle) - 1
            next_marble += num_in_batch
        else:
            # add the batch
            num_in_batch = num_to_remove
            cycle = cycle[:insert_position] + \
                    list(itertools.chain(
                        *zip(cycle[insert_position:(insert_position + num_in_batch)],
                             range(next_marble, next_marble + num_in_batch)))) + \
                    cycle[(insert_position + num_in_batch):]
            current_position = insert_position + (num_in_batch * 2) - 1

            # remove multiple of 23
            cycle_len = len(cycle)
            remove_position = (current_position - 7) % cycle_len
            scores[(current_to_remove - 1) % n_player] += current_to_remove + cycle.pop(
                remove_position)

            next_marble = current_to_remove + 1
            current_to_remove += 23
            current_position = remove_position % (cycle_len - 1)
    return max(scores)
