day = 4

###############################
from collections import Counter
lower = 168630
upper = 718098


# Part One
def is_valid(password):
    psw = str(password)
    for idx, digit in enumerate(psw[:-1]):
        if digit == psw[idx + 1]:
            break
    else:
        return False

    for idx, digit in enumerate(psw[:-1]):
        if digit > psw[idx + 1]:
            return False

    return True


def part1():
    return sum(is_valid(p) for p in range(lower, upper + 1))


print(part1())


# Part Two
def is_valid_2(password):
    psw = str(password)

    for idx, digit in enumerate(psw[:-1]):
        if digit > psw[idx + 1]:
            return False

    return 2 in Counter(psw).values()


def part2():
    return sum(is_valid_2(p) for p in range(lower, upper + 1))


print(part2())
