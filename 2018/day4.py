day = 4

###############################
from read_input import *

input_string = get_input_string(day)
logs = input_string.splitlines()
logs.sort()

guards_log = {}
guards_sleep_time = {}
for log in logs:
    time, status = log.split(']')
    minute = int(time[-2:])
    if 'Guard' in status:
        uid = int(status.split('#')[1].split(' ')[0])
    elif 'falls asleep' in status:
        sleep = minute
    elif 'wakes up' in status:
        wake = minute
        log = guards_log.get(uid, {})
        sleep_time = guards_sleep_time.get(uid, 0)
        for time in range(sleep, wake):
            log[time] = log.get(time, 0) + 1
        guards_log[uid] = log
        guards_sleep_time[uid] = sleep_time + (wake - sleep)


# Part One
def find_key_with_max_value(dic):
    reverse_dic = {v:k for k, v in dic.items()}
    max_key = max(reverse_dic.keys())
    return reverse_dic[max_key]


guard = find_key_with_max_value(guards_sleep_time)
minute = find_key_with_max_value(guards_log[guard])
print(guard * minute)


# Part Two
max_guard = None
max_minute = None
max_freq = 0
for guard, log in guards_log.items():
    for minute, freq in log.items():
        if freq > max_freq:
            max_freq = freq
            max_guard = guard
            max_minute = minute

print(max_guard * max_minute)
