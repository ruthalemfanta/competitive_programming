# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smaller = ListNode()
        larger = ListNode()
        smaller_dummy = smaller
        larger_dummy = larger

        while head:
            if head.val < x:
                smaller_dummy.next = head
                smaller_dummy = smaller_dummy.next
            else:
                larger_dummy.next = head
                larger_dummy = larger_dummy.next

            head = head.next

        smaller_dummy.next = larger.next
        larger_dummy.next = None 

        return smaller.next
