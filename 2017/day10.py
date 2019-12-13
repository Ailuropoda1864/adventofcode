from functools import reduce
import operator



TEST = '/home/fay/Downloads/test.txt'


# pt 1
def twist(lengths):
    l = list(range(256))
    cur_pos, skip = 0, 0
    for length in lengths:
        end = cur_pos + length
        if end < len(l):
            l = l[:cur_pos] + l[cur_pos: end][::-1] + l[end:]
        else:
            end -= len(l)
            r = l[:end][::-1] + l[cur_pos:][::-1]
            l = r[length-end:] + l[end: cur_pos] + r[:length-end]
        cur_pos += length + skip
        if cur_pos >= len(l):
            cur_pos -= len(l)
        skip += 1
    return l[0] * l[1]


# pt 2
def knot_hash(string):
    l = list(range(256))
    cur_pos, skip = 0, 0
    lengths = [ord(char) for char in string] + [17, 31, 73, 47, 23]

    for _ in range(64):
        for length in lengths:
            end = cur_pos + length
            if end < len(l):
                l = l[:cur_pos] + l[cur_pos: end][::-1] + l[end:]
            else:
                end %= len(l)
                r = l[:end][::-1] + l[cur_pos:][::-1]
                l = r[length-end:] + l[end: cur_pos] + r[:length-end]
            cur_pos += length + skip
            if cur_pos >= len(l):
                cur_pos %= len(l)
            skip += 1

    dense = [reduce(lambda x, y: operator.xor(x, y), l[index: index+16])
             for index in range(0, 256, 16)]

    return ''.join(['{:02x}'.format(num) for num in dense])
