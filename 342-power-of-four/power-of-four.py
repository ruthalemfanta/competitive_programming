class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        def four(n):
            if n == 1:
                return True
            if n % 4 != 0:
                return False
            return four(n//4)

        return four(n)