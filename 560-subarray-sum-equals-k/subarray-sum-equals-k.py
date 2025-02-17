from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = 0
        summ = 0
        track = defaultdict(int)
        track[0] = 1
        for num in nums:
            summ += num
            count += track[summ - k]
            track[summ] += 1
        return count

