from collections import Counter
def minSteps(s, t) -> int:
    p = Counter(s)
    q = Counter(t)
    steps = 0

    for i in p:
        if i in q:
            if p[i] > q[i]:
                steps += p[i] - q[i]
        else:
            steps += p[i] 

    return steps
    
        
s = 'leetcode'
t = 'practice'

print(minSteps(s, t))
