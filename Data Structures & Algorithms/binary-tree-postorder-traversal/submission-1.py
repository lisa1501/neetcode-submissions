# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            
            node = stack.pop() #1,3,7,6,2,5,4

            res.append(node.val) #res=[1,3,7,6,2,5,4]

            if node.left:#2
                stack.append(node.left) #stack =[]

            if node.right:
                stack.append(node.right) #stack =[]

        return res[::-1]
        