# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [[root,subRoot]]
        while stack:
            nodeP, nodeQ = stack.pop()

            if nodeP is None and nodeQ is None:
                continue

            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False


            stack.append([nodeP.left, nodeQ.left])
            stack.append([nodeP.right, nodeQ.right])
        return True