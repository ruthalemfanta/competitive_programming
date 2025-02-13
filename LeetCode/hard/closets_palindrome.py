
def nearestPalindromic(n):
    length = len(n)
    if n == "1":
        return "0"

    candidates = set()
    candidates.add(str(10**(length-1) - 1))
    candidates.add(str(10**length + 1))

    prefix = int(n[:(length + 1) // 2])

    for i in [-1, 0, 1]:
        candidate = str(prefix + i)
        if length % 2 == 0:
            candidates.add(candidate + candidate[::-1])
        else:
            candidates.add(candidate + candidate[:-1][::-1])

    candidates.discard(n)  

    def difference(x):
        return abs(int(x) - int(n)), int(x) 

    return min(candidates, key=difference)

n="123"
print(nearestPalindromic(n))
