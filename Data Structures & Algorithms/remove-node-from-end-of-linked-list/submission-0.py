# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        cur = head

        while n > 0:
            cur = cur.next
            n -= 1

        while cur:
            prev = prev.next
            cur = cur.next

        
        prev.next = prev.next.next

        return dummy.next
        