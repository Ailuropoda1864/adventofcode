# pt 1
def count_steps(lst):
    num_steps = 0
    index = 0
    pointer = 0
    while pointer < len(lst) and pointer >= 0:
        pointer += lst[index]
        lst[index] += 1
        num_steps += 1
        index = pointer
    return num_steps


def read_inst(file, func):
    with open(file) as f:
        return func([int(num) for num in f])


# pt 2
def count_steps2(lst):
    num_steps = 0
    index = 0
    pointer = 0
    while pointer < len(lst) and pointer >= 0:
        pointer += lst[index]
        if lst[index] >= 3:
            lst[index] -= 1
        else:
            lst[index] += 1
        num_steps += 1
        index = pointer
    return num_steps
