from itertools import combinations


TEST = '/home/fay/Downloads/test.txt'


# pt 1
def parse_components(file):
    with open(file) as f:
        return [Component(line.strip()) for line in f]


class Component(object):
    def __init__(self, name):
        self.ports = tuple(map(int, name.split('/')))


def build_edges(components):
    edges = {}
    for c1, c2 in combinations(components, 2):
        for num1, port1 in enumerate(c1.ports):
            for num2, port2 in enumerate(c2.ports):
                if port1 == port2:
                    edges[(c1, num1)] = edges.get((c1, num1), []) + [(c2, num2)]
                    edges[(c2, num2)] = edges.get((c2, num2), []) + [(c1, num1)]
    return edges


class TreeNode(object):
    def __init__(self, component, parent, port_to_parent):
        """
        :param Component component: Reference to bridge component
        :param TreeNode parent: Reference to parent tree node object
        """
        self.component = component
        self.parent = parent
        self.port_to_parent = port_to_parent
        self.children = set()
        self._used_component_set = None

    @property
    def used_component_set(self):
        if self._used_component_set is None:
            s = set([self.component])
            if self.parent is not None:
                s |= self.parent.used_component_set
            self._used_component_set = s
        return self._used_component_set

    def add_children(self, components, edges, tree_nodes):
        compatible = edges.get((self.component, 1 - self.port_to_parent), [])
        available = set(components) - self.used_component_set
        for component, port in compatible:
            if component in available:
                child = TreeNode(component, self, port)
                self.children.add(child)
                tree_nodes.append(child)


def build_tree(components, edges):
    tree_nodes = []
    for component in components:
        if 0 in component.ports:
            node = TreeNode(component, None, component.ports.index(0))
            tree_nodes.append(node)

    i = 0
    while i < len(tree_nodes):
        tree_nodes[i].add_children(components, edges, tree_nodes)
        i += 1

    return tree_nodes


def cal_strength(bridge):
    return sum([port for component in bridge for port in component.ports])


def find_strongest_bridge(nodes):
    max_strength = -1
    for node in nodes:
        if len(node.children) == 0:
            strength = cal_strength(node.used_component_set)
            if strength > max_strength:
                max_strength = strength
    return max_strength


# pt 2
def find_longest_bridge(nodes):
    max_len = 0
    for node in nodes:
        if len(node.children) == 0:
            bridge = node.used_component_set
            if len(bridge) > max_len:
                max_len = len(bridge)
                max_strength = cal_strength(bridge)
            elif len(bridge) == max_len:
                strength = cal_strength(bridge)
                if strength > max_strength:
                    max_strength = strength
    return max_strength


def main():
    components = parse_components(TEST)
    edges = build_edges(components)
    tree_nodes = build_tree(components, edges)

    # pt 1
    print(find_strongest_bridge(tree_nodes))

    # pt 2
    print(find_longest_bridge(tree_nodes))


if __name__ == '__main__':
    main()
