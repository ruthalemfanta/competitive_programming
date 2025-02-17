class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = maxx = nums[0]

        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            maxx = max(maxx, cur_sum)

        return maxx