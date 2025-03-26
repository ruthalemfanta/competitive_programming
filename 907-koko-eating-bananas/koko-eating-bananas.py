class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 1

        def good(rate):
            total_time = 0
            for pile in piles:
                total_time += ceil(pile / rate)

            return total_time <= h

        while left <= right:
            mid = (left + right) // 2

            if good(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


        