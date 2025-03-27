class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            count = 1
            cur_sum = 0
            for weight in weights:
                cur_sum += weight
                if cur_sum > capacity:
                    cur_sum = weight
                    count += 1
            print(count, capacity)
            return count

        left = max(weights)
        right = sum(weights)
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if valid(mid) <= days:
                ans = min(ans, mid)
                right = mid - 1
            elif valid(mid) > days:
                left = mid + 1

        return ans



        