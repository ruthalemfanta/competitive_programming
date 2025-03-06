class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s, reverse = True)

        if s[0] == 0:
            return ''
        for i in range(len(s)):
            if s[i] == '0':
                s[i - 1], s[-1] = s[-1], s[i - 1]
                break

        return ''.join(s)