class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        stack = []
        for i in range(rowIndex + 1):
            if not stack:
                stack.append([1])
                continue
            if len(stack) == 1:
                stack.append([1,1])
                continue

            prev = stack[-1]
            row = [1] * (len(prev) + 1)
            for j in range(1, len(row)-1):
                row[j] = prev[j-1] + prev[j]

            stack.append(row)

        return stack.pop()

        
