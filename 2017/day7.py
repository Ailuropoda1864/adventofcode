# pt 1
import re


class Disc(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.total_weight = None
        self.loads = None
        self.load_counts = None
        self.parent = None

    def is_child(self, other):
        if self.name in other.children:
            self.parent = other
            return True
        return False

    def sum_weight(self, nodes):
        if self.total_weight is None:
            self.loads = [nodes[child].sum_weight(nodes)
                          for child in self.children]
            self.total_weight = sum(self.loads) + self.weight
        return self.total_weight

    def is_balanced(self, nodes):
        counts = {}
        for index, load in enumerate(self.loads):
            counts[load] = counts.get(load, []) + [nodes[self.children[index]]]
        self.load_counts = counts
        if len(counts) > 1:
            return False
        return True


def parse_line(line):
    pattern = r'([a-z]+) \(([0-9]+)\)( -> (.+))?'
    match = re.match(pattern, line)
    children = []
    if match.group(3):
        children = [name.strip() for name in match.group(4).split(',')]
    return Disc(match.group(1), int(match.group(2)), children)


def build_nodes(file):
    with open(file) as f:
        nodes = {}
        for line in f:
            disc = parse_line(line)
            nodes[disc.name] = disc
        return nodes


def find_root(nodes):
    nodes = list(nodes.values())
    for index1, node1 in enumerate(nodes[:-1]):
        index2 = index1 + 1
        while index2 < len(nodes):
            node2 = nodes[index2]
            if not node1.is_child(node2):
                node2.is_child(node1)
            index2 += 1

    for node in nodes:
        if node.parent is None:
            return node


# pt 2
def find_unbalanced_nodes(nodes):
    min_weight = float('inf')
    for node in list(nodes.values()):
        node.sum_weight(nodes)
        if not node.is_balanced(nodes):
            if node.total_weight < min_weight:
                min_weight = node.total_weight
                min_node = node
    return min_node


def correct_weight(node):
    for k, v in node.load_counts.items():
        if len(v) > 1:
            total_weight = k
        else:
            culprit = v[0]

    return total_weight - culprit.total_weight + culprit.weight
