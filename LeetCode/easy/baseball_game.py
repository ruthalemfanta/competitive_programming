def calPoints(operations):
    score = []
    for i in operations:
        if i == '+' and score:
            score.append(score[-1] + score[-2])
        elif i == 'D' and score:
            score.append(score[-1] * 2)
        elif i == 'C' and score:
            score.pop()
        else:
            score.append(int(i))
    return sum(score)

operations = ["5","2","C","D","+"]
print(calPoints(operations)) # 30
        
