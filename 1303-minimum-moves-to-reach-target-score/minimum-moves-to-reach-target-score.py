class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        if maxDoubles == 0:
            return target - 1
        
        while target != 1 and maxDoubles:
            moves += target % 2
            target = target // 2
            moves += 1
            maxDoubles -= 1

        moves = moves + target - 1
        return moves
