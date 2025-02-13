from collections import Counter

def majorityElement(nums):
    num_count = Counter(nums)
    majorityEle, count = num_count.most_common(1)[0]

    return majorityEle


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))