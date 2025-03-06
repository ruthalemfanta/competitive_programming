from collections import defaultdict
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1

            if freq['R'] == freq['L']:
                count += 1
                left = right + 1

        return count 

