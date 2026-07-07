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
        def heigh(node):
            h = 0
            while node.parent:
                h += 1
                node = node.parent
            return h
        h1 = heigh(p)
        h2 = heigh(q)

        if h1 > h2:
            p, q = q, p
        diff = abs(h1 - h2)
        while diff:
            q = q.parent
            diff -= 1
        
        while p != q:
            p = p.parent
            q = q.parent
        return p