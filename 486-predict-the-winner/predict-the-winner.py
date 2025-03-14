class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        states = {}
        def turn(left, right, player):
            if (left, right, player) in states:
                return states[(left, right, player)]
            if left > right:
                return 0
            if player:
                states[(left, right, player)] = max(nums[left] + turn(left + 1, right, not player), nums[right] + turn(left, right - 1, not player ))
                return states[(left, right, player)]
            else:
                states[(left, right, player)] = min(-nums[left] + turn(left + 1, right, not player), -nums[right] + turn(left, right - 1, not player ))
                return states[(left, right, player)]

        return turn(0, len(nums)-1, True) >= 0



