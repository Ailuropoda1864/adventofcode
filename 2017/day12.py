TEST = '/home/fay/Downloads/test.txt'


# pt 1
def parse_input(file):
    graph = {}
    with open(file) as f:
        for line in f:
            nodes = line.strip().split(' <-> ')
            graph[nodes[0]] = nodes[1].split(', ')
    return graph


def grouping(graph, id='0'):
    to_do = graph[id]
    group = {id}
    while to_do:
        program = to_do.pop()
        if program not in group:
            group.add(program)
            to_do += graph[program]
    return group


# pt 2
def num_groups(graph):
    num_groups = 0
    programs = set(graph.keys())
    while programs:
        program = programs.pop()
        group = grouping(graph, program)
        num_groups += 1
        programs -= group
    return num_groups

def main():
    print(len(grouping(parse_input(TEST))))
    print(num_groups(parse_input(TEST)))


if __name__ == '__main__':
    main()

