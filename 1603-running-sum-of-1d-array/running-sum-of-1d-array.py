class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []

        for i in range(1, len(nums) + 1):
            running.append(sum(nums[:i]))

        return running 