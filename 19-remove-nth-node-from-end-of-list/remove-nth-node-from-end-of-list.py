# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        count=0
        while cur:
            cur=cur.next
            count+=1
        print(count)
        index = count-n

        cur =head
        count=0
        if not head:
            return
        elif not head.next:
            if index == 0:
                head = None
                return
            else:
                return

        if index == 0 and head.next:
            head = head.next
        while cur and cur.next:
            if count == index-1:
                cur.next = cur.next.next

            count+=1
            cur=cur.next
        return head    