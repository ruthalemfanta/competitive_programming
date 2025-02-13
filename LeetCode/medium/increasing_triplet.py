def increasingTriplet(nums):
    if len(nums) == 1:
        return True
    return nums[0] < nums[1] and increasingTriplet(nums[1:])


print(increasingTriplet([1,2,3,4,5])) 