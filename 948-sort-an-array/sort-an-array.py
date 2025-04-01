class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:     
        def merge_split(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_split(arr[:mid])
            right = merge_split(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            

            return res + left[i:] +right[j:]

        return merge_split(nums)