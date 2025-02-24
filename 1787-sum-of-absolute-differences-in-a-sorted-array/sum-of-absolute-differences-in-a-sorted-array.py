class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        res = []
        for i in range(len(nums)):
            left = prefix[i] - nums[i]
            right = prefix[-1] - prefix[i]
            
            left_c = i
            right_c = len(nums) - 1 - i
            
            left_t = left_c * nums[i] - left
            right_t = right - right_c * nums[i]

            res.append(left_t + right_t)
        
        return res