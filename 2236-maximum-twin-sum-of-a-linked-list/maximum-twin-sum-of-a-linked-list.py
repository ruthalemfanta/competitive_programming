# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        maxx = 0

        while curr:
            arr.append(curr.val)
            curr = curr.next

        rev = arr[::-1]

        for i in range(len(arr)):
            maxx = max(maxx, arr[i] + rev[i])

        return maxx

