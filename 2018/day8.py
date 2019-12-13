day = 8

###############################
from read_input import *

input_string = get_input_string(day)
input_list = list(map(int, input_string.split()))


class Node:
    def __init__(self, parent, n_children, n_meta):
        self.parent = parent
        self.n_children = n_children
        self.n_meta = n_meta
        self.children = []
        self.metadata = []

    def __repr__(self):
        return 'n_children: {} | n_meta: {}'.format(
            self.n_children, self.n_meta)

    @property
    def total(self):
        return sum(self.metadata) + sum(child.total for child in self.children)

    @property
    def value(self):
        if self.children:
            return sum(self.children[index-1].value for index in self.metadata
                       if 0 < index <= len(self.children))
        else:
            return sum(self.metadata)


# build nodes
root = Node(None, input_list[0], input_list[1])

current_node = root
i = 2  # index of the input list

# traverse the input list to build the remaining nodes
length = len(input_list)
while i < length:
    if current_node.n_children > len(current_node.children):
        current_node.children.append(Node(current_node, input_list[i], input_list[i + 1]))
        current_node = current_node.children[-1]
        i += 2
    else:
        current_node.metadata = [input_list[i + _] for _ in range(current_node.n_meta)]
        i += current_node.n_meta
        current_node = current_node.parent


def part1():
    return root.total


def part2():
    return root.value


if __name__ == '__main__':
    print(part1())
    print(part2())
