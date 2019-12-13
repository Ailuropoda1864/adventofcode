# pt 1
def find_nk(number):
    n = int((number ** 0.5 - 1) / 2)
    return n, n * 2 + 1


def steps(number):
    n, k = find_nk(number)
    remain = number - k ** 2

    if remain == 0:
        return 2 * n

    side = k + 1
    n += 1
    remain %= side
    return abs(n) + abs(remain - n)


# pt 2
def fill_grid(number):
    x, y, n = 0, 0, 0
    square = {(0, 0): 1}
    while True:
        last = (2 * n + 1) ** 2
        side = 2 * n + 2
        x += 1

        while len(square) - last < side:
            fill = fill_next(x, y, square)
            if fill > number:
                return fill
            square[(x, y)] = fill
            y += 1

        y -= 1

        while len(square) - last < 2 * side:
            x -= 1
            fill = fill_next(x, y, square)
            if fill > number:
                return fill
            square[(x, y)] = fill

        while len(square) - last < 3 * side:
            y -= 1
            fill = fill_next(x, y, square)
            if fill > number:
                return fill
            square[(x, y)] = fill

        while len(square) - last < 4 * side:
            x += 1
            fill = fill_next(x, y, square)
            if fill > number:
                return fill
            square[(x, y)] = fill

        n += 1


def fill_next(x, y, square):
    total = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            total += square.get((i, j), 0)
    return total
