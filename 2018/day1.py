day = 1

###############################
from read_input import *

input_string = get_input_string(day)

freq_change_list = list(map(int, input_string.splitlines()))


# Part One
print(sum(freq_change_list))


# Part Two
from time import time


def find_first_repeat_freq(freq_change_list):
    current_freq = 0
    resulting_freqs = {0}

    i = 0
    length = len(freq_change_list)
    while True:
        current_freq += freq_change_list[i]
        if current_freq in resulting_freqs:
            return current_freq
        else:
            resulting_freqs.add(current_freq)
            # i = (i + 1) % length
            i = i + 1 if i < length - 1 else 0


start = time()
print(find_first_repeat_freq(freq_change_list))
print(time()-start)


# Alternative for Part Two
from itertools import cycle


def find_first_repeat_freq_2(freq_change_list):
    current_freq = 0
    resulting_freqs = {0}

    for freq_change in cycle(freq_change_list):
        current_freq += freq_change
        if current_freq in resulting_freqs:
            return current_freq
        else:
            resulting_freqs.add(current_freq)


start = time()
print(find_first_repeat_freq_2(freq_change_list))
print(time()-start)
