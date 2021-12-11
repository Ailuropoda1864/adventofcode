DAY = 4

###############################
from read_input import *


class Board:
    def __init__(self, five_lines: list):
        self.xy_to_num = {
            (x, y): num
            for y, line in enumerate(five_lines)
            for x, num in enumerate(line.split())
        }
        self.num_to_xy = {
            v: {"xy": k, "marked": False} for k, v in self.xy_to_num.items()
        }
        self.marked_x = {i: 0 for i in range(5)}
        self.marked_y = {i: 0 for i in range(5)}
        self.bingo = False

    def __repr__(self):
        output = "Board:\n"
        for y in range(5):
            for x in range(5):
                num = self.xy_to_num[(x, y)]
                if self.num_to_xy[num]["marked"]:
                    num = f"_{num}_"
                output += num + " "
            output += "\n"
        return output + "\n"

    def mark(self, num):
        if num in self.num_to_xy.keys():
            x, y = self.num_to_xy[num]["xy"]
            self.num_to_xy[num]["marked"] = True
            self.marked_x[x] += 1
            if self.marked_x[x] == 5:
                self.bingo = True
            self.marked_y[y] += 1
            if self.marked_y[y] == 5:
                self.bingo = True

    def sum_of_unmarked(self):
        return sum(
            (
                int(num)
                for num, attr in self.num_to_xy.items()
                if attr["marked"] is False
            )
        )


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    lines = input_string.splitlines()
    random_numbers = lines[0].split(",")
    boards = [Board(lines[i : i + 5]) for i in range(2, len(lines), 6)]
    return random_numbers, boards


def part1(random_numbers, boards):
    for n in random_numbers:
        for board in boards:
            board.mark(n)
            if board.bingo:
                return board.sum_of_unmarked() * int(n)


def part2(random_numbers, boards):
    unwin_boards = set(range(len(boards)))
    for n in random_numbers:
        for idx in list(unwin_boards):
            boards[idx].mark(n)
            if boards[idx].bingo:
                most_recently_won_board = idx
                unwin_boards.remove(idx)
        if len(unwin_boards) == 0:
            return boards[most_recently_won_board].sum_of_unmarked() * int(n)


if __name__ == "__main__":
    # Part 1
    random_numbers, boards = parse_input(test=False)
    print(part1(random_numbers, boards))
    # Part 2
    random_numbers, boards = parse_input(test=False)
    print(part2(random_numbers, boards))
