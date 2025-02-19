# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        size=0
        while cur:
            cur=cur.next
            size+=1
        if size % 2 == 0:
            index = (size // 2) 
        else:
            index = size // 2

        if not head:
            return

        count = 0
        cur = head
        while cur:
            if index ==count:
                return cur
            count+=1
            cur=cur.next    
        return head
    