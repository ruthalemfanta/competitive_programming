class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def isValid(ball): 
            start = -1e100
            count = 0
            for p in position:
                if p - start >= ball:
                    start = p
                    count += 1
            
            return count >= m

        left = 0
        right = position[-1] 
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
        