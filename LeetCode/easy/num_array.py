class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        if right != len(self.nums) - 1:
            return sum(self.nums[left:right+1])
        else:
            return sum(self.nums[left:])   
        


nums = [-2, 0, 3, -5, 2, -1]
left = 2
right = 5        

obj = NumArray(nums)
param_1 = obj.sumRange(left,right)
print(param_1)