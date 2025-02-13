
def numberOfPairs(nums, target):
    pairs = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i !=j:
                pairs += 1

    return pairs

    
nums = ["777","7","77","77"]
target = '7777'

print(numberOfPairs(nums, target))