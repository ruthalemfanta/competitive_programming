from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0 
        summ = 0
        prefix = defaultdict(int)
        prefix[0]  = 1

        for num in nums:
            summ += num
            count += prefix[summ - goal]
            prefix[summ] += 1

        return count 
        