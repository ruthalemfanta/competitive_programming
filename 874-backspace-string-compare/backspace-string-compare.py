class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        for i in range(len(s)):
            if s[i] == '#' and stacks:
                stacks.pop()
            elif s[i] == '#' and not stacks:
                continue
            else:
                stacks.append(s[i])
        for i in range(len(t)):
            if t[i] == '#' and stackt:
                stackt.pop()
            elif t[i] == '#' and not stackt:
                continue
            else:
                stackt.append(t[i])

        print(stacks, stackt)
        return stacks == stackt 
