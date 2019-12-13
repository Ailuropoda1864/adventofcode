# pt 1
def reallocate(banks):
    configs = [banks[:]]

    while True:
        max_mem = max(banks)
        max_index = banks.index(max_mem)
        banks[max_index] = 0

        while max_mem > 0:
            max_index += 1
            if max_index >= len(banks):
                max_index -= len(banks)
            banks[max_index] += 1
            max_mem -= 1

        if banks in configs:
            return len(configs)

        configs.append(banks[:])


# pt 2
def loop_size(banks):
    configs = [banks[:]]

    while True:
        max_mem = max(banks)
        max_index = banks.index(max_mem)
        banks[max_index] = 0

        small_share, big_allo = divmod(max_mem, len(banks))
        small_allo = len(banks) - big_allo
        for i in range(max_index - small_allo + 1, max_index+1):
             banks[i] += small_share
        for i in range(max_index+1, max_index+big_allo+1):
            try:
                banks[i] += small_share + 1
            except IndexError:
                banks[i-len(banks)] += small_share + 1

        if banks in configs:
            return len(configs) - configs.index(banks)

        configs.append(banks[:])
