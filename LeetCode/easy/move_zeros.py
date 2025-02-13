def moveZeros(nums):
    zero_count = 0
    i = 0 
    while i < len(nums):
        if nums[i] == 0:
            zero_count += 1
            nums.pop(i)
        else:
            i += 1

    for i in range(zero_count):
        nums.append(0)
    
    return nums
        



nums = [0,0,1]

print(moveZeros(nums))