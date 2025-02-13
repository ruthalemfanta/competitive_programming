def reverseWords(S):
    s = s.split(' ') 
    n = len(s)
    i = 0
    while i < n:
        if i == 0 and s[i] == '':
            del s[i]
            n = n - 1
        elif i == n - 1 and s[i] == '':
            del s[i]
            n = n - 1
        elif s[i] == '':
            del s[i]
            n = n - 1
        else:
            i = i + 1


    s = s[::-1]
    return ' '.join(s) 