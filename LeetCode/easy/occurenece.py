from collections import Counter

def test(arr):

    c = Counter(arr)

    c = list(c.values())

    return len(c) == len(set(c))


