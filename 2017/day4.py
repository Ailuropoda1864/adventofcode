# pt 1
def is_valid(pph):
    words = pph.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        if word_count[word] > 1:
            return False
    return True


def count_valid(file, func):
    with open(file) as f:
        return sum([func(line) for line in f])


# pt 2
def element_count(els):
    el_count = {}
    for el in els:
        el_count[el] = el_count.get(el, 0) + 1
    return el_count


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    if set(word1) != set(word2):
        return False
    dict1, dict2 = map(element_count, [word1, word2])
    for key, value in dict1.items():
        if value != dict2[key]:
            return False
    return True


def is_valid2(pph):
    words = pph.split()
    for index1, word1 in enumerate(words[:-1]):
        index2 = index1 + 1
        while index2 < len(words):
            if is_anagram(word1, words[index2]):
                return False
            index2 += 1
    return True
