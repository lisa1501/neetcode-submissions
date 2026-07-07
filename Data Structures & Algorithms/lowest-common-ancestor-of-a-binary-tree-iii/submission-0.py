"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr1, ptr2 = p, q #3,12
        while ptr1 != ptr2:
            if ptr1: 
                ptr1 = ptr1.parent #5#None#1#3
            else:
                ptr1 = q #12

            if ptr2:
                ptr2 = ptr2.parent #1#3#5#None
            else:
                ptr2 = p #3

        return ptr1
        