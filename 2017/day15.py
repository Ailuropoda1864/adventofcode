# pt 1
def generator(num, multiplier):
    while True:
        num = num * multiplier % 2147483647
        yield num


def lowest_16_bits(num):
    return bin(num)[-16:]


def num_matches(num_a, num_b, sample_size = 40 * 10 ** 6):
    count = 0
    a = generator(num_a, 16807)
    b = generator(num_b, 48271)
    for i in range(sample_size):
        if lowest_16_bits(next(a)) == lowest_16_bits(next(b)):
            count += 1
    return count


# pt 2
def generator2(num, multiplier, divider):
    while True:
        num = num * multiplier % 2147483647
        if num % divider == 0:
            yield num


def num_matches2(num_a, divider_a, num_b, divider_b, sample_size = 5 * 10 ** 6):
    count = 0
    a = generator2(num_a, 16807, divider_a)
    b = generator2(num_b, 48271, divider_b)
    for i in range(sample_size):
        if lowest_16_bits(next(a)) == lowest_16_bits(next(b)):
            count += 1
    return count


def main():
    print(num_matches(618, 814))
    print(num_matches2(618, 4, 814, 8))


if __name__ == '__main__':
    main()