import string


TEST = '/home/fay/Downloads/test.txt'

# pt 1
def read_maze(file):
    with open(file) as f:
        return [line.strip('\n') for line in f]


def is_within_bound(i, j, maze):
    return 0 <= i < len(maze) and 0 <= j < len(maze[0])


def walk_maze(maze):
    letters = []
    i, j = 0, maze[0].index('|')
    direction = 1

    while True:
        # walk in up-down directions
        while maze[i][j] not in ' +':
            if maze[i][j] in string.ascii_uppercase:
                letters.append(maze[i][j])
            i += direction
            if not is_within_bound(i, j, maze):
                return ''.join(letters)

        # turn left/right
        if is_within_bound(i, j-1, maze) and maze[i][j-1] != ' ':
            direction = -1
        elif is_within_bound(i, j+1, maze) and maze[i][j+1] != ' ':
            direction = 1
        else:
            return ''.join(letters)
        j += direction

        # walk in left-right directions
        while maze[i][j] not in ' +':
            if maze[i][j] in string.ascii_uppercase:
                letters.append(maze[i][j])
            j += direction
            if not is_within_bound(i, j, maze):
                return ''.join(letters)

        # turn up/down
        if is_within_bound(i-1, j, maze) and maze[i-1][j] != ' ':
            direction = -1
        elif is_within_bound(i+1, j, maze) and maze[i+1][j] != ' ':
            direction = 1
        else:
            return ''.join(letters)
        i += direction


# pt 2
def count_steps(maze):
    num_steps = 0
    i, j = 0, maze[0].index('|')
    direction = 1

    while True:
        # walk in up-down directions
        while maze[i][j] not in ' +':
            i += direction
            if not is_within_bound(i, j, maze):
                return num_steps
            num_steps += 1

        # turn left/right
        if is_within_bound(i, j-1, maze) and maze[i][j-1] != ' ':
            direction = -1
        elif is_within_bound(i, j+1, maze) and maze[i][j+1] != ' ':
            direction = 1
        else:
            return num_steps
        j += direction
        num_steps += 1

        # walk in left-right directions
        while maze[i][j] not in '+ ':
            j += direction
            if not is_within_bound(i, j, maze):
                return num_steps
            num_steps += 1

        # turn up/down
        if is_within_bound(i-1, j, maze) and maze[i-1][j] != ' ':
            direction = -1
        elif is_within_bound(i+1, j, maze) and maze[i+1][j] != ' ':
            direction = 1
        else:
            return num_steps
        i += direction
        num_steps += 1


def main():
    # pt 1
    maze = read_maze(TEST)
    print(walk_maze(maze))

    # pt 2
    print(count_steps(maze))


if __name__ == '__main__':
    main()



