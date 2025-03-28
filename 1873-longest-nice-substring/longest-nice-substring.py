class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divide(s):
            if len(s) <= 1:
                return ''
            set_s = set(s)
            for i, letter in enumerate(s):
                case_letter = letter.swapcase()
                if case_letter not in set_s:
                    left = divide(s[:i])
                    right = divide(s[i+1:])
                    if len(left) >= len(right):
                        return left
                    return right
            return s
            
        return divide(s) 

