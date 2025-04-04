class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def merge(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge(nums[:mid])
            right = merge(nums[mid:])

            i = 0
            j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            return res + left[i:] + right[j:]

        numb = merge(nums)

        for i in range(len(numb)):
            if numb[i] != i :
                return i

        return numb[-1] + 1
        

