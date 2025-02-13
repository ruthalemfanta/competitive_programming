def removeStars(s):
    stack = []

    for l in s:
        if l == '*':
            stack.pop()
        else:
            stack.append(l)


    return ''.join(stack)
s = 'leet**cod*e'
print(removeStars(s))

    
        