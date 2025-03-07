class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)+int(b))
            elif char == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)-int(b))
            elif char == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)*int(b))
            elif char == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a)/int(b))
            else:
                stack.append(char)

        return int(stack[0])
        