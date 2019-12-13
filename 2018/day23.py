day = 23

###############################
from read_input import *
import re
from collections import Counter


input_string = get_input_string(day)

# input_string = '''pos=<10,12,12>, r=2
# pos=<12,14,12>, r=2
# pos=<16,12,12>, r=4
# pos=<14,14,14>, r=6
# pos=<50,50,50>, r=200
# pos=<10,10,10>, r=5'''


class Nanobot:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def get_distance(self, other):
        return sum(
            map(abs, [self.x - other.x, self.y - other.y, self.z - other.z]))

    def is_in_range(self, other):
        return self.get_distance(other) <= self.r


def parse_input(input_str):
    split_input = input_str.splitlines()
    pattern = re.compile(r'pos=<([-0-9]+),([-0-9]+),([-0-9]+)>, r=([-0-9]+)')
    return [Nanobot(*map(int, pattern.match(line).groups())) for line in split_input]


def get_strongest_bot(nanobots):
    return max(nanobots, key=lambda bot: bot.r)


def part1(nanobots):
    strongest_robot = get_strongest_bot(nanobots)
    return sum(strongest_robot.is_in_range(bot) for bot in nanobots)



def get_coords_in_range(bot):
    return {(x, y, z)
            for delta_x in range(bot.r + 1)
            for delta_y in range(bot.r - delta_x + 1)
            for delta_z in range(bot.r - delta_x - delta_y + 1)
            for x in (bot.x - delta_x, bot.x + delta_x)
            for y in (bot.y - delta_y, bot.y + delta_y)
            for z in (bot.z - delta_z, bot.z + delta_z)}


def part2(nanobots):
    range_to_consider = get_coords_in_range(get_strongest_bot(nanobots))
    count = {}
    for coord in range_to_consider:
        for bot in nanobots:
            if bot.is_in_range(Nanobot(*coord, 0)):
                count[coord] = count.get(coord, 0) + 1
    return max(count, key=lambda coord: count[coord])


if __name__ == '__main__':
    nanobots = parse_input(input_string)
    print(part1(nanobots))
    print(part2(nanobots))