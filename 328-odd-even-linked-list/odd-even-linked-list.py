# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        curr = head
        even = curr.next
        index = 0 
        prev = None
        while curr.next:
            index += 1
            next_node = curr.next 
            curr.next = curr.next.next
            prev = curr
            curr = next_node

        if index % 2 != 0:
            prev.next = even
        else:
            curr.next = even

        return head


