def test(nums):
    left = 0
    zeros = 0
    result = 0

    if 0 not in nums:
        return len(nums) - 1
    elif 1 not in nums:
        return 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        result = max(result, right - left )

    return result

print(test([1,1,0,1]))

        
        
