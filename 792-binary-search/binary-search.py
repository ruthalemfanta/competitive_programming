class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        def helper(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                # print(mid,left,right)
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return helper(mid + 1, right, target)
                else:
                    return helper(left, mid - 1, target)
            return -1
        return helper(left, right, target)

            
            
        