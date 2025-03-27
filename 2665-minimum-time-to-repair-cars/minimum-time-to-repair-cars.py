class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def isValid(time):
            total = 0
            for rank in ranks:
                n = floor(sqrt(time/rank))
                total += n

            return total

        left = 0
        right = min(ranks) * (cars * cars)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if isValid(mid) >= cars:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans

        


        