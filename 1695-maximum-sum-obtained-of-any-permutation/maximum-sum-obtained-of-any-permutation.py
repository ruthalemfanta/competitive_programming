class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        diff = [0] * (len(nums) + 1)

        for left, right in requests:
            diff[left] += 1

            if right + 1 < len(nums):
                diff[right + 1] -= 1

        prefix = []
        acc = 0
        nums.sort
        for num in diff:
            acc += num
            prefix.append(acc)

        summ = 0
        for rate, amount in zip(sorted(prefix[:-1]), sorted(nums)):
            summ += rate * amount
        
        return summ % (10 ** 9 + 7)


    