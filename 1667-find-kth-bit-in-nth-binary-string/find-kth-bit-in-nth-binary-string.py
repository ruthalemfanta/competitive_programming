class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        stack = []
        for i in range(n):
            if not stack:
                stack.append('0')
                continue
            invert = ''
            for i in range(len(stack[-1])):
                if stack[-1][i] == '0':
                    invert += '1'
                else:
                    invert += '0'

            res = stack[-1] + '1' + invert[::-1]
            stack.append(res)


        return stack[-1][k - 1]


