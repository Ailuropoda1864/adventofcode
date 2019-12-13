day = 6

###############################
from read_input import *

input_string = get_input_string(day)
input_list = input_string.splitlines()


class Map:
    def __init__(self, lst):
        self.nodes = {}

        for line in lst:
            parent, child = line.split(')')
            self.nodes[parent] = self.nodes.get(parent, Obj(parent))
            self.nodes[child] = self.nodes.get(child, Obj(child))
            self.nodes[parent].add_child(self.nodes[child])
            self.nodes[child].add_parent(self.nodes[parent])


class Obj:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_parent(self, other):
        self.parent = other
        return self

    def add_child(self, other):
        self.children.append(other)
        return self

    @property
    def total_orbits(self):
        if self.parent is None:
            return 0
        else:
            return 1 + self.parent.total_orbits

    @property
    def ancestors(self):
        if self.parent is None:
            return []
        else:
            return [self.parent.name] + self.parent.ancestors


m = Map(input_list)


# Part One
print(sum(n.total_orbits for n in m.nodes.values()))


# Part Two
a1 = m.nodes['YOU'].ancestors
a2 = m.nodes['SAN'].ancestors
common_ancestors = set(a1) & set(a2)
print(min(a1.index(a) + a2.index(a)for a in common_ancestors))
