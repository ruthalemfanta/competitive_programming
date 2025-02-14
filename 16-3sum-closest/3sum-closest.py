class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minn = float('inf')

        if sum(nums[:3]) > target:
            return sum(nums[:3])
        elif sum(nums[-3:]) < target:
            return sum(nums[-3:])

        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums) - 1

            while left<right:
                summ = nums[i] + nums[left] + nums[right]
                if abs(summ-target) < abs(minn-target):
                    minn = summ
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else:
                    return summ
        return minn

