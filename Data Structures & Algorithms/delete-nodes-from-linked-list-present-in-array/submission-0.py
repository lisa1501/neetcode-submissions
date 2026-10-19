# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        cur = head
        while cur:
            next_node = cur.next
            cur.next = None
            if cur.val not in nums:
                prev.next = cur
                prev = cur

            cur = next_node
        return dummy.next


