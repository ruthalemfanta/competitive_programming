from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        summ = 0 
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            summ += num
            count += prefix[summ%k]
            prefix[summ%k] += 1

        return count 

