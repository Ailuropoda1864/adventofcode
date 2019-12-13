day = 14

###############################
from read_input import *

input_string = get_input_string(day)


def part1(n_recipe):
    scores = [3, 7]
    length = len(scores)
    elf1, elf2 = 0, 1
    target_length = n_recipe + 10

    while length < target_length:
        new_score = scores[elf1] + scores[elf2]
        if new_score > 9:
            scores.append(new_score // 10)
            scores.append(new_score % 10)
            length += 2
        else:
            scores.append(new_score)
            length += 1

        elf1 = (elf1 + 1 + scores[elf1]) % length
        elf2 = (elf2 + 1 + scores[elf2]) % length

    return ''.join(map(str, scores[n_recipe: (n_recipe + 10)]))


def part2(input_score):
    input_length = len(input_score)
    scores = [3, 7]
    length = len(scores)
    elf1, elf2 = 0, 1

    while True:
        new_score = scores[elf1] + scores[elf2]
        if new_score > 9:
            scores.append(new_score // 10)
            scores.append(new_score % 10)
            length += 2
            if scores[-input_length-1: -1] == input_score:
                return length - 1 - input_length
            elif scores[-input_length:] == input_score:
                return length - input_length

        else:
            scores.append(new_score)
            length += 1
            if scores[-input_length:] == input_score:
                return length - input_length

        elf1 = (elf1 + 1 + scores[elf1]) % length
        elf2 = (elf2 + 1 + scores[elf2]) % length


if __name__ == '__main__':
    # Part One
    n_recipe = int(input_string)
    print(part1(n_recipe))

    # Part Two
    input_score = list(map(int, list(input_string.strip())))
    print(part2(input_score))
