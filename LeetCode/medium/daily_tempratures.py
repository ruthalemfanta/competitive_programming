def temperature(temperatures):
    answer = []
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
        answer.append(0)
    return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(temperature(temperatures))  
