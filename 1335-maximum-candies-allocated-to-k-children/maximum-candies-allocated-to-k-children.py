class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
  
        candies.sort()
        def good(pile):
            count = 0
            for cand in candies:
                count += cand // pile
            return count >= k

        left = 1
        right = max(candies)
        ans = 0
        while left <= right:
            mid = (right + left) // 2
            if good(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans