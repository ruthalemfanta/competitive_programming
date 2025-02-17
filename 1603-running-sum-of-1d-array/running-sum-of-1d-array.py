class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        summ = 0 

        for num in nums:
            summ += num
            running.append(summ)

        return running 