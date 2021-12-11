DAY = 5

###############################
from collections import Counter
from read_input import *


class Line:
    def __init__(self, lst, simple_mode):
        self.x1, self.y1, self.x2, self.y2 = lst
        self.points = self.get_points(simple_mode)

    def __repr__(self):
        return f"Line: ({self.x1}, {self.y1}), ({self.x2}, {self.y2})"

    @staticmethod
    def __sort_coordinate(value1, value2):
        if value1 >= value2:
            return value1, value2
        else:
            return value2, value1

    def get_points(self, simple_mode):
        x_max, x_min = self.__sort_coordinate(self.x1, self.x2)
        y_max, y_min = self.__sort_coordinate(self.y1, self.y2)
        if x_min == x_max or y_min == y_max:
            return [
                (x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)
            ]
        elif simple_mode:
            return []
        else:
            assert y_max - y_min == x_max - x_min
            return [
                (
                    self.x1 + i * (self.x2 - self.x1) / abs(self.x2 - self.x1),
                    self.y1 + i * (self.y2 - self.y1) / abs(self.y2 - self.y1),
                )
                for i in range(y_max - y_min + 1)
            ]


def parse_input(test: bool, simple_mode=True):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    input_lines = input_string.splitlines()
    lines = []
    for line in input_lines:
        dot1, dot2 = line.split(" -> ")
        x1, y1 = dot1.split(",")
        x2, y2 = dot2.split(",")
        lines.append(Line(map(int, [x1, y1, x2, y2]), simple_mode))
    return lines


def count_overlap_points(lines):
    tally = Counter()
    for line in lines:
        tally.update(Counter(line.points))
    return sum((1 for v in tally.values() if v >= 2))


if __name__ == "__main__":
    # Part 1
    lines = parse_input(test=False)
    print(count_overlap_points(lines))
    # Part 2
    lines = parse_input(test=False, simple_mode=False)
    print(count_overlap_points(lines))
