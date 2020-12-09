day = 7

###############################
import re
from read_input import *

input_string = get_input_string(day)
# input_string = read_file('test.txt')

input_list = input_string.splitlines()


class Bag:
    members = {}
    def __init__(self, color):
        self.color = color
        self.children = {}
        self.parents = []

    def find_ancestors(self, explored=None, to_explore=None):
        if to_explore is None:
            to_explore = self.parents[:]
        if explored is None:
            explored = set()
        if len(to_explore) == 0:
            return explored
        else:
            head = to_explore.pop()
            explored.add(head)
            for p in Bag.members[head].parents:
                if p not in explored:
                    to_explore.append(p)
            return self.find_ancestors(explored, to_explore)

    @property
    def offspring_count(self):
        """This count includes oneself"""
        if len(self.children) == 0:
            return 1
        else:
            return 1 + sum(
                Bag.members[child].offspring_count * count
                for child, count in self.children.items()
            )


def match_child_pattern(string):
    pattern = r'(?P<num_child>\d+) (?P<child>[a-z ]+) bags*\.*'
    return re.fullmatch(pattern, string)


def parse(input_list):
    for rule in input_list:
        parent, children = rule.split(' bags contain ')
        children_list = children.split(', ')
        Bag.members[parent] = Bag.members.get(parent, Bag(parent))
        if children_list[0] != 'no other bags.':
            children = {
                match.group('child'): int(match.group('num_child'))
                for match in map(match_child_pattern, children_list)
            }
            Bag.members[parent].children.update(children)
            for child in children.keys():
                if child not in Bag.members.keys():
                    Bag.members[child] = Bag(child)
                Bag.members[child].parents.append(parent)


def part1(color):
    return len(Bag.members[color].find_ancestors())


def part2(color):
    return Bag.members[color].offspring_count - 1


if __name__ == '__main__':
    parse(input_list)
    print(part1('shiny gold'))
    print(part2('shiny gold'))
