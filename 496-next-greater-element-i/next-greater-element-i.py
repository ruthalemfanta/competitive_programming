class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        mono = []

        for num in nums2:
            while mono and mono[-1] < num:
                p = mono.pop()
                freq[p] = num

            mono.append(num)

        ans = []

        for num in nums1:
            if num not in freq:
                ans.append(-1)
            else:
                ans.append(freq[num])

        return ans