DAY = 12

###############################
from collections import Counter
from read_input import *


class Cave:
    def __init__(self, name):
        self.name = name
        self.is_big_cave = name.upper() == name
        self.neighbors = set()

    def __repr__(self):
        return self.name


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    caves = {}
    for line in input_string.splitlines():
        name1, name2 = line.split("-")
        if name1 not in caves:
            caves[name1] = Cave(name1)
        if name2 not in caves:
            caves[name2] = Cave(name2)
        caves[name1].neighbors.add(name2)
        caves[name2].neighbors.add(name1)
    return caves


def traverse(current_cave, visited, paths, validate_func):
    for next_cave in caves[current_cave].neighbors:
        if next_cave == "end":
            visited.append(next_cave)
            paths.append(visited[:])
            visited.pop()
        elif validate_func(next_cave, visited, caves):
            visited.append(next_cave)
            traverse(next_cave, visited, paths, validate_func)
    visited.pop()


def validate_part1(cave, visited, caves):
    return caves[cave].is_big_cave or cave not in visited


def validate_part2(cave, visited, caves):
    if caves[cave].is_big_cave or cave not in visited:
        return True
    elif cave in ("start", "end"):
        return False
    else:
        small_caves = Counter(
            [
                visited_cave
                for visited_cave in visited
                if not caves[visited_cave].is_big_cave
            ]
        )
        return all([count < 2 for count in small_caves.values()])


if __name__ == "__main__":
    caves = parse_input(test=False)
    # Part 1
    paths = []
    traverse("start", ["start"], paths, validate_part1)
    print(len(paths))
    # Part 2
    paths = []
    traverse("start", ["start"], paths, validate_part2)
    print(len(paths))
