DAY = 5

###############################
import re
import copy

from read_input import *


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)
    stacks = {}
    instructions = []
    for line in input_string.splitlines():
        if "[" in line:
            for i in range(0, len(line), 4):
                if line[i + 1] != " ":
                    stack_name = str(i // 4 + 1)
                    stacks[stack_name] = stacks.get(stack_name, []) + [line[i + 1]]
        elif "move" in line:
            result = re.match(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", line,)
            instructions.append(result.groups())
    return stacks, instructions


def part1(stacks, instructions):
    for ins in instructions:
        num_crates, from_stack, to_stack = ins
        num_crates = int(num_crates)
        for i in range(num_crates):
            stacks[to_stack] = [stacks[from_stack].pop(0)] + stacks[to_stack]
    return "".join(stacks[str(j + 1)][0] for j in range(len(stacks)))


def part2(stacks, instructions):
    for ins in instructions:
        num_crates, from_stack, to_stack = ins
        num_crates = int(num_crates)
        crates_to_be_moved = stacks[from_stack][:num_crates]
        stacks[from_stack] = stacks[from_stack][num_crates:]
        stacks[to_stack] = crates_to_be_moved + stacks[to_stack]
    return "".join(stacks[str(j + 1)][0] for j in range(len(stacks)))


if __name__ == "__main__":
    stacks, instructions = parse_input(test=False)
    # Part 1
    print(part1(copy.deepcopy(stacks), instructions))
    # Part 2
    print(part2(copy.deepcopy(stacks), instructions))
