DAY = 11

###############################
from read_input import *


class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = int(energy)
        self.flash = False

    def check_flash(self, octopuses):
        if self.energy > 9:
            self.flash = True
            self.energy = 0
            for j in range(self.y - 1, self.y + 2):
                for i in range(self.x - 1, self.x + 2):
                    if (i, j) != (self.x, self.y) and (i, j) in octopuses:
                        octopuses[(i, j)].energy += 1
                        octopuses[(i, j)].check_flash(octopuses)


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    return {
        (x, y): Octopus(x, y, energy)
        for y, line in enumerate(input_string.splitlines())
        for x, energy in enumerate(line)
    }


def part1(octopuses, steps):
    flash_count = 0
    for _ in range(steps):
        for k in octopuses.keys():
            octopuses[k].energy += 1
            octopuses[k].check_flash(octopuses)
        for k in octopuses:
            if octopuses[k].flash:
                flash_count += 1
                octopuses[k].energy = 0
                octopuses[k].flash = False
    return flash_count


def part2(octopuses):
    step = 0
    while True:
        step += 1
        for k in octopuses.keys():
            octopuses[k].energy += 1
            octopuses[k].check_flash(octopuses)
        for k in octopuses:
            if octopuses[k].flash:
                octopuses[k].energy = 0
                octopuses[k].flash = False
        if all([o.energy == 0 for o in octopuses.values()]):
            return step


if __name__ == "__main__":
    # Part 1
    octopuses = parse_input(test=False)
    print(part1(octopuses, 100))
    # Part 2
    octopuses = parse_input(test=False)
    print(part2(octopuses))
