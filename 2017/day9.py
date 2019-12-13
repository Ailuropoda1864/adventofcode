# pt 1
def score(string):
    index, score, level = 0, 0, 0
    while index < len(string):
        if string[index] == '<':
            while string[index] != '>':
                if string[index] == '!':
                    index += 1
                index += 1
        if string[index] == '{':
            level += 1
            score += level
        if string[index] == '}':
            level -= 1
        index += 1
    return score


def garbage(string):
    index, count = 0, 0
    while index < len(string):
        if string[index] == '<':
            start = index
            escape = 0
            while string[index] != '>':
                if string[index] == '!':
                    index += 1
                    escape += 2
                index += 1
            count += index - start - escape - 1
        index += 1
    return count
