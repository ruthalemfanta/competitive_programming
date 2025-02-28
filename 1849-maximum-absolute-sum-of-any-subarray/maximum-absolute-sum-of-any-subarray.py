class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_prefix = 0
        min_prefix = 0
        curr = 0
        for num in nums:
            curr += num
            max_prefix = max(max_prefix, curr)
            min_prefix = min(min_prefix, curr)

        return abs(max_prefix - min_prefix)