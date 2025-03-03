class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) < 3:
            return 0

        if len(nums) == 3:
            if nums[0] + nums[1] <= nums[2]:
                return 0
            else:
                return sum(nums)

        r = len(nums) - 1

        for i in range(len(nums) - 2, 0, -1):
            if nums[i] + nums[i - 1] > nums[r]:
                return nums[i] + nums[i - 1] + nums[r]
            r -= 1

        return 0