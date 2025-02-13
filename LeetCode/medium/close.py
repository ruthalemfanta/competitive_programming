from collections import Counter


def close(word1, word2):
    w1 = Counter(word1)
    w2 = Counter(word2)

    if set(word1) != set(word2):
        return False
    
    if len(word1) != len(word2):
        return False
    
    if sorted(w1.values()) != sorted(w2.values()):
        return False
    
    return True


word1 = "abc"
word2 = "cba"

print(close(word1, word2))