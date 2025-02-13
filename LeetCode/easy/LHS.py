def maxArray(n):
    max_val = n[0]
    min_val = n[0]
    for i in range(len(n)):
        if n[i] > max_val:
            max_val = n[i]
        elif n[i] < min_val:
            min_val = n[i]
            
    return max_val - min_val == 1

def subArray(n):
    subArrays = []
    for i in range(len(n)):
        for j in range(i+1, len(n)+1):
            subArrays.append(n[i:j])
    
    return subArrays

def LHS(n):
    max_length = 0
    for sub in subArray(n):
        if maxArray(sub):
            max_length = max(max_length, len(sub))
    
    return max_length

n = [1,3,2,2,5,2,3,7]
print(LHS(n))  # Output should be the length of the longest harmonious subarray
