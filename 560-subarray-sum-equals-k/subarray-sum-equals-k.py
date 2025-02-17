from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        summ = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for num in nums:
            summ += num
            count += prefix[summ - k]
            prefix[summ] += 1
        return count

