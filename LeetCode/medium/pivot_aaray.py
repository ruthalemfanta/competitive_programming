def pivotArray(nums, pivot):
    left = []
    right = []
    between = []

    for i in nums:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            between.append(i)

    return left + between + right

nums = [9, 12, 3, 5, 14, 10, 10]
pivot = 10

print(pivotArray(nums, pivot))  
