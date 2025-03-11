class Solution:
    def trailingZeroes(self, n: int) -> int:
        def trailing(n):
            if n < 5:
                return 0
            return n//5 + trailing(n//5)

        return trailing(n)