class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        left = 0
        sort_p = sorted(p)

        sub = s[:k]
        ana = 0 
        index = []
        for right in range(k, len(s) + 1):

            sub_c = sub[:]
            if sorted(sub_c) == sort_p:
                ana += 1
                index.append(left)
            if right < len(s):
                left += 1
                sub = sub[1:] + s[right]



        return index
