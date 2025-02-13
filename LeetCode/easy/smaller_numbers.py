#get the current 
#compare it to the others
#store it in an array index

def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0 
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)
        
    return result

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))