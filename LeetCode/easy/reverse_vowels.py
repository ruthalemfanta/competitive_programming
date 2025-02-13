def reverseVowels(s):
    order = []
    arr = list(s)
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            order.append(i)
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            arr[i] = s[order.pop()]

    return ''.join(arr)

print(test("hello")) # "holle"
