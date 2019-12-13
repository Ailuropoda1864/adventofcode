# pt 1
def spinlock(n_steps, n_inserts):
    cycle = [0]
    cur_pos = 0
    for i in range(1, n_inserts + 1):
        cur_pos = (cur_pos + n_steps) % i + 1
        cycle = cycle[:cur_pos] + [i] + cycle[cur_pos:]
    return cycle[cur_pos + 1]


# pt 2
def spinlock2(n_steps, n_inserts):
    cur_pos = 0
    num_after_0 = []
    for i in range(1, n_inserts + 1):
        cur_pos = (cur_pos + n_steps) % i + 1
        if cur_pos == 1:
            num_after_0.append(i)
    return num_after_0[-1]


def main():
    print(spinlock(366, 2017))
    print(spinlock2(366, 50000000))


if __name__ == '__main__':
    main()