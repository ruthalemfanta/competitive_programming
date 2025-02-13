def smallestEvenMultiple(n):
    arr = []
    i = 1
    while True:
        if i%n == 0 and i%2==0:
            arr.append(i)
            break
        i+=1

    return arr[0]

result = smallestEvenMultiple(6)
print(result) 

            