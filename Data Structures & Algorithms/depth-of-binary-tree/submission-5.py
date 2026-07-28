# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            return 1 + max(left, right)
        return dfs(root)



    # def minDepth(self, root: Optional[TreeNode]) -> int:
    #     def dfs(node):
    #         if node node:
    #             return 0
    #         left = dfs(node.left)
    #         right = dfs(node.right)
    #         if not node.left:
    #             return 1 + right
    #         if not node.right:
    #             return 1 + left
    #         return 1+min(left, right)
    #     return dfs(root)

    
        