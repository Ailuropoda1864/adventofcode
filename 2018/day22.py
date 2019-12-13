DEPTH = 6084
MOUTH = (0, 0)
TARGET = (14, 709)


def get_geologic_index(x, y, e_lvl=None):
    if e_lvl is None:
        e_lvl = {}
    if (x, y) in (MOUTH, TARGET):
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return e_lvl[(x - 1, y)] * e_lvl[(x, y - 1)]


def get_region_types():
    erosion_levels = {}
    for y in range(TARGET[1] + 1):
        for x in range(TARGET[0] + 1):
            g_idx = get_geologic_index(x, y, erosion_levels)
            erosion_levels[(x, y)] = (g_idx + DEPTH) % 20183
    return [[erosion_levels[(x, y)] % 3 for x in range(TARGET[0] + 1)]
            for y in range(TARGET[1] + 1)]


def part1():
    area = get_region_types()
    return sum(sum(row) for row in area)


if __name__ == '__main__':
    print(part1())


