TEST = '/home/fay/Downloads/test.txt'


# pt 1
def load_file(file):
    with open(file) as f:
        return f.read().strip().split(',')


# def final_coors(paths):
#     height = 0.75 ** 0.5
#     directions = {
#         'n': lambda x, y: (x, y + 2 * height),
#         's': lambda x, y: (x, y - 2 * height),
#         'nw': lambda x, y: (x - 1.5, y + height),
#         'ne': lambda x, y: (x + 1.5, y + height),
#         'sw': lambda x, y: (x - 1.5, y - height),
#         'se': lambda x, y: (x + 1.5, y - height)
#     }
#
#     a, b = 0, 0
#     for path in paths:
#         a, b = directions[path](a, b)
#
#     return a, b
#
#
# def cal_steps(a, b):
#     height = 0.75 ** 0.5
#     a, b = abs(a), abs(b)
#     if a == 0:
#         return b / (2 * height)
#     elif b == 0:
#         return a / 3 * 2
#     else:
#         return cal_steps(a - 1.5, b - height) + 1
#
#
# def furthest(paths):
#     height = 0.75 ** 0.5
#     directions = {
#         'n': lambda x, y: (x, y + 2 * height),
#         's': lambda x, y: (x, y - 2 * height),
#         'nw': lambda x, y: (x - 1.5, y + height),
#         'ne': lambda x, y: (x + 1.5, y + height),
#         'sw': lambda x, y: (x - 1.5, y - height),
#         'se': lambda x, y: (x + 1.5, y - height)
#     }
#
#     a, b, max_steps = 0, 0, 0
#     for path in paths:
#         a, b = directions[path](a, b)
#         num_steps = cal_steps(a, b)
#         if num_steps > max_steps:
#             max_steps = num_steps
#
#     return max_steps


def final_coors(paths):
    directions = {
        'n': lambda x, y: (x, y + 1),
        's': lambda x, y: (x, y - 1),
        'nw': lambda x, y: (x - 1, y),
        'ne': lambda x, y: (x + 1, y + 1),
        'sw': lambda x, y: (x - 1, y - 1),
        'se': lambda x, y: (x + 1, y)
    }

    a, b = 0, 0
    for path in paths:
        a, b = directions[path](a, b)

    return a, b


def cal_steps(a, b):
    product = a * b
    a, b = abs(a), abs(b)
    if product < 0:
        return a + b
    else:
        return max(a, b)


# pt 2
def furthest(paths):
    directions = {
        'n': lambda x, y: (x, y + 1),
        's': lambda x, y: (x, y - 1),
        'nw': lambda x, y: (x - 1, y),
        'ne': lambda x, y: (x + 1, y + 1),
        'sw': lambda x, y: (x - 1, y - 1),
        'se': lambda x, y: (x + 1, y)
    }

    a, b, max_steps = 0, 0, 0
    for path in paths:
        a, b = directions[path](a, b)
        num_steps = cal_steps(a, b)
        if num_steps > max_steps:
            max_steps = num_steps
    return max_steps


print(cal_steps(*final_coors(load_file(TEST))))
print(round(furthest(load_file(TEST))))
