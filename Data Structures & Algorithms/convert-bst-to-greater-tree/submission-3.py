# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        curr = root
        greaterSum = 0

        while stack or curr:

            # Traverse to the largest node
            while curr:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()

            greaterSum += curr.val
            curr.val = greaterSum

            # Move to left subtree
            curr = curr.left

        return root