def productExceptSelf(nums):
    answer = [1] * len(nums)
    left = 1
    for i in range(len(nums)):
        answer[i] = left
        left *= nums[i]

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))
