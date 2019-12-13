day = 18

###############################
from read_input import *

input_string = get_input_string(day)
split_input = input_string.splitlines()


class Acre:
    area = {}

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.next_state = state

    def determine_next_state(self):
        adj_acres = [self.area[(x, y)].state for x in range(self.x - 1, self.x + 2)
                     for y in range(self.y - 1, self.y + 2)
                     if (x, y) in self.area.keys() and not (x == self.x and y == self.y)]

        if self.state == '.':
            if adj_acres.count('|') >= 3:
                self.next_state = '|'
        elif self.state == '|':
            if adj_acres.count('#') >= 3:
                self.next_state = '#'
        elif self.next_state == '#':
            if '#' not in adj_acres or '|' not in adj_acres:
                self.next_state = '.'

    def change_state(self):
        self.state = self.next_state
        self.area[(self.x, self.y)] = self


def parse_input(split_input):
    for y, line in enumerate(split_input):
        for x, char in enumerate(line):
            Acre.area[x, y] = Acre(x, y, char)


def simulate(split_input, n_iter=10):
    parse_input(split_input)
    areas = [''.join(split_input)]
    i = 0
    while i < n_iter:
        for acre in Acre.area.values():
            acre.determine_next_state()
        for acre in Acre.area.values():
            acre.change_state()
        i += 1
        area = ''.join(Acre.area[key].state for key in sorted(
            Acre.area.keys(), key=lambda coords: (coords[1], coords[0])))
        if area not in areas:
            areas.append(area)
        else:
            break
    if i < n_iter:
        idx = areas.index(area)
        area = areas[(n_iter - i) % (i - idx) + idx]
    else:
        area = areas[-1]
    return area.count('|') * area.count('#')



if __name__ == '__main__':
    # Part One
    print(simulate(split_input))
    # Part Two
    print(simulate(split_input, 1000000000))
