class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                left_s = s[:left] + s[left+1:]
                right_s = s[:right] + s[right+1:]
                if left_s == left_s[::-1] or right_s == right_s[::-1]:
                    return True
                else:
                    return False
        
        return True
                