class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def query_check(k):
            summ = 0
            diff = [0] * (len(nums) + 1)

            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val

            for i in range(len(nums)):
                summ += diff[i]
                if summ < nums[i]:
                    return False
            return True

        if not query_check(len(queries)):
            return -1

        left = 0
        right = len(queries)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if query_check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
