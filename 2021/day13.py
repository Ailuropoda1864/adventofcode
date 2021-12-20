DAY = 13

###############################
from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    dots = []
    folds = []
    for line in input_string.splitlines():
        if line.strip() == "":
            continue
        elif "fold along" in line:
            axis, value = line.replace("fold along ", "").split("=")
            folds.append((axis, int(value)))
        else:
            dots.append(tuple(map(int, line.split(","))))
    return dots, folds


def transform(dots, fold_direction, fold_line):
    new_dots = []
    if fold_direction == "y":
        for x, y in dots:
            if y > fold_line:
                new_dots.append((x, 2 * fold_line - y))
            elif y < fold_line:
                new_dots.append((x, y))
    elif fold_direction == "x":
        for x, y in dots:
            if x > fold_line:
                new_dots.append((2 * fold_line - x, y))
            elif x < fold_line:
                new_dots.append((x, y))
    return list(set(new_dots))


def part1(dots, folds):
    fold_direction, fold_line = folds[0]
    return len(transform(dots, fold_direction, fold_line))


def format_dots(dots):
    xs = [x for x, _ in dots]
    ys = [y for _, y in dots]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    output = ""
    for j in range(min_y, max_y + 1):
        for i in range(min_x, max_x + 1):
            if (i, j) in dots:
                output += "#"
            else:
                output += " "
        output += "\n"
    return output


def part2(dots, folds):
    for fold_direction, fold_line in folds:
        dots = transform(dots, fold_direction, fold_line)
    return format_dots(dots)


if __name__ == "__main__":
    # Part 1
    dots, folds = parse_input(test=False)
    print(part1(dots, folds))
    # Part 2
    print(part2(dots, folds))
