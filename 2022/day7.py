DAY = 7

###############################
import re

from read_input import *


class SystemObject:
    file_system = {}

    def __init__(self, path: tuple, object_type: str, size=None):
        self.path = path
        self.object_type = object_type
        self.cached_size = size
        self.children = set()

    def __repr__(self):
        return f"{self.object_type}: {'/'.join(self.path)}"

    @property
    def size(self):
        if self.cached_size is None:
            self.cached_size = sum(
                SystemObject.file_system[child].size for child in self.children
            )
        return self.cached_size


def parse_input(test: bool):
    if test:
        input_string = read_file("test.txt")
    else:
        input_string = get_input_string(DAY)

    cwd = tuple()
    for line in input_string.splitlines():
        # command
        if line[0] == "$":
            if line.rstrip() == "$ cd ..":
                cwd = cwd[:-1]
            elif line.rstrip() == "$ ls":
                pass
            else:
                m = re.match(r"\$ cd (.+)", line)
                if m:
                    dir_path = tuple(list(cwd) + [m.group(1)])
                    SystemObject.file_system[dir_path] = SystemObject(dir_path, "dir")
                    if cwd:
                        SystemObject.file_system[cwd].children.add(dir_path)
                    cwd = dir_path
                else:
                    raise Exception(
                        f"command not recognized: {line.strip('$').strip()}"
                    )
        # outputs
        else:
            if line[:3] == "dir":
                dir_path = tuple(list(cwd) + [line[4:].strip()])
                SystemObject.file_system[dir_path] = SystemObject(dir_path, "dir")
                SystemObject.file_system[cwd].children.add(dir_path)
            else:
                m_file = re.match(r"([0-9]+) (.+)", line)
                if m_file:
                    file_size = int(m_file.group(1))
                    file_path = tuple(list(cwd) + [m_file.group(2)])
                    SystemObject.file_system[file_path] = SystemObject(
                        file_path, "file", file_size
                    )
                    if cwd:
                        SystemObject.file_system[cwd].children.add(file_path)
                else:
                    raise Exception(f"output not recognized: {line}")
    return SystemObject.file_system


def part1(file_system):
    return sum(
        v.size
        for v in file_system.values()
        if v.object_type == "dir" and v.size <= 100000
    )


def part2(file_system):
    min_to_delete = file_system[("/",)].size - (70000000 - 30000000)
    assert min_to_delete >= 0
    return min(
        v.size
        for v in file_system.values()
        if v.object_type == "dir" and v.size >= min_to_delete
    )


if __name__ == "__main__":
    file_system = parse_input(test=False)
    # Part 1
    print(part1(file_system))
    # Part 2
    print(part2(file_system))
