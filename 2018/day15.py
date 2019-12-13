day = 15

###############################
from collections import abc, deque
from functools import total_ordering

from read_input import *


input_string = get_input_string(day)


@total_ordering
class Space:
    room = {}

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adj_spaces = []
        self.unit = None
        self.tree_node = None

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y < other.y

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __repr__(self):
        return f'<Space x={self.x} y={self.y} unit={self.unit}>'

    def get_available_adj_spaces(self, symbol):
        return [s for s in self.adj_spaces
                if s.unit is None or s.unit.symbol != symbol]

    def is_next_to_enemy(self, other_unit):
        return any(s.unit.symbol != other_unit.symbol
                   for s in self.adj_spaces
                   if s.unit)


class TreeNode(abc.Container):
    def __init__(self, space):
        self.space = space
        self.parent = None
        self.children = []
        self.space.tree_node = self

    def get_path_to_root(self, path=None):
        path = [] if path is None else path
        path.append(self.space)
        if self.parent is None:
            return path
        else:
            return self.parent.get_path_to_root(path)

    def add_child(self, other):
        self.children.append(other)
        other.parent = self

    def __repr__(self):
        return f'<TreeNode parent={self.parent}, space={self.space}>'

    def __contains__(self, item):
        return (item == self.space or
                any(child.__contains__(item) for child in self.children))

    def get_steps(self, i=0):
        if self.parent is None:
            return i
        else:
            return self.parent.get_steps(i + 1)


@total_ordering
class Unit:
    attack_power = 3
    symbol = None

    def __init__(self, space):
        self.space = space
        self.hit_points = 200

    def __lt__(self, other):
        return self.space < other.space

    def __eq__(self, other):
        return self.space == other.space

    def __repr__(self):
        return f'<Unit symbol={self.symbol} ap={self.attack_power} hp={self.hit_points} x={self.space.x}, y={self.space.y}>'
    
    def is_enemy(self, other):
        if other is None:
            return False
        return self.symbol != other.symbol

    @property
    def attack_target(self):
        adj_enemies = [space.unit for space in self.space.adj_spaces
                       if self.is_enemy(space.unit)]
        if adj_enemies:
            return min(adj_enemies, key=lambda u: (u.hit_points, u.space))
        else:
            return None

    def attack(self, target):
        if target is not None:
            target.hit_points -= self.attack_power
            if target.hit_points <= 0:
                target.space.unit = None
            return True
        return False

    def move(self):
        path_from_enemy = self.get_path_from_nearest_enemy()
        if path_from_enemy:
            next_space = path_from_enemy[-2]
            self.space.unit = None
            self.space = next_space
            next_space.unit = self
            return True
        return False

    def get_bfs_shortest_paths(self):
        queue = deque([self.space])
        tree = TreeNode(self.space)
        paths = []
        min_steps = sys.maxsize
        while queue:
            head_space = queue.popleft()
            tree_node = head_space.tree_node
            steps = tree_node.get_steps()
            if steps > min_steps:
                break
            if head_space.is_next_to_enemy(self):
                min_steps = steps
                paths.append(tuple(tree_node.get_path_to_root()))
            for space in sorted(s for s in head_space.get_available_adj_spaces(self.symbol)
                                if s not in tree and s not in queue):
                queue.append(space)
                tree_node.add_child(TreeNode(space))
        return paths

    def get_path_from_nearest_enemy(self):
        paths = self.get_bfs_shortest_paths()
        if paths:
            return min(paths, key=lambda path: (path[0], path[-2]))
        else:
            return []

    def take_action(self):
        action_taken = False
        if self.hit_points > 0:
            action_taken = self.attack(self.attack_target)
            if not action_taken:
                action_taken = self.move()
                self.attack(self.attack_target)
        return action_taken


def parse_input(input_str, part_2=False, elf_attack=3):
    Gremlin.part2 = part_2
    Elf.attack_power = elf_attack
    split_input = input_str.splitlines()
    units = []
    for y, line in enumerate(split_input):
        for x, char in enumerate(line):
            if char in 'EG.':
                space = Space.room.get((x, y), Space(x, y))
                Space.room[(x, y)] = space
                for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                    neighbor_char = split_input[ny][nx]
                    if neighbor_char in 'EG.':
                        neighbor = Space.room.get((nx, ny), Space(nx, ny))
                        Space.room[(nx, ny)] = neighbor
                        space.adj_spaces.append(neighbor)
                if char in 'EG':
                    UnitClass = Elf if char == 'E' else Gremlin
                    units.append(UnitClass(space))
                    space.unit = units[-1]
    return units


def run_battle(units):
    rounds = 0
    actions_taken = []
    while len({unit.symbol for unit in units}) > 1:
        actions_taken = [unit.take_action() for unit in units]
        units = sorted(unit for unit in units if unit.hit_points > 0)
        rounds += 1
    if not actions_taken[-1]:
        rounds -= 1
    return rounds * sum(u.hit_points for u in units)


class Elf(Unit):
    symbol = 'E'


class Gremlin(Unit):
    symbol = 'G'
    part2 = False

    def attack(self, target):
        retval = super().attack(target)
        if Gremlin.part2 and retval and target.hit_points <= 0:
            raise ValueError('An elf died')
        return retval


def parse_input2(input_str, E_att_pwr):
    Elf.attack_power = E_att_pwr
    split_input = input_str.splitlines()
    units = []
    for y, line in enumerate(split_input):
        for x, char in enumerate(line):
            if char in 'EG.':
                space = Space.room.get((x, y), Space(x, y))
                Space.room[(x, y)] = space
                for nx, ny in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
                    neighbor_char = split_input[ny][nx]
                    if neighbor_char in 'EG.':
                        neighbor = Space.room.get((nx, ny), Space(nx, ny))
                        Space.room[(nx, ny)] = neighbor
                        space.adj_spaces.append(neighbor)
                if char in 'EG':
                    unit_class = Elf if char == 'E' else Gremlin
                    units.append(unit_class(char, space))
                    space.unit = units[-1]
    return units


def run_new_battle(units):
    rounds = 0
    actions_taken = []
    while len({unit.symbol for unit in units}) > 1:
        print(sorted([(u.symbol, u.hit_points, u.space.x, u.space.y) for u in units], key=lambda u: u[1]))
        try:
            actions_taken = [unit.take_action() for unit in units]
        except ValueError:
            return None

        units = sorted(unit for unit in units if unit.hit_points > 0)
        rounds += 1
    if not actions_taken[-1]:
        rounds -= 1
    return rounds, sum(u.hit_points for u in units)


def part2(input_str):
    E_att_pwr = 4
    while True:
        print(f'Trying power level {E_att_pwr}')
        units = parse_input(input_string, True, E_att_pwr)
        try:
            return run_battle(units)
        except ValueError:
            E_att_pwr += 1


if __name__ == '__main__':
    input_string = get_input_string_from_file('test.txt')
    # # Part One
    # units = parse_input(input_string)
    # print(run_battle(units))

    print(part2(input_string))
