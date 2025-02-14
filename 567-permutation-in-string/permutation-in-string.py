class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0 
        for right in range(k,len(s2)+1):
            if sorted(s2[left:right]) == sorted(s1):
                return True
            left += 1

        return False



        