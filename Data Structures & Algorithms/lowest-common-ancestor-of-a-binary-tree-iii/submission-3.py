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
        # Input: root = [5,3,4,2,1,null,9,null,11,10,12], p = 3, q = 12
        parent_p = p 
        parent_q = q 
        # parent_p =3,  5, None, 12, 1,    3,
        # parent_q =12, 1,  3,    5, None, 3,

        while parent_p != parent_q: 
            

            if parent_p:
                parent_p = parent_p.parent 
            else:
                 parent_p = q 

            if parent_q:
                parent_q = parent_q.parent 
            else:
                 parent_q = p
            
        return parent_p