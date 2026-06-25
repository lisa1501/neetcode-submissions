# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.children = children

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter


    # def diameterOfNrayTree(self, root: Optional[TreeNode]) -> int:
    #     diameter = 0

    #     def dfs(node):
    #         nonlocal diameter

    #         if not node:
    #             return 0

    #         h1 = 0
    #         h2 = 0

    #         for ch in node.children:
    #             h = dfs(ch)
    #             if h > h1:
    #                 h1 = h
    #                 h2 = h1
    #             if h1 > h > h2:
    #                 h2 = h


    #         diameter = max(diameter, h1 + h2)

    #         return 1 + max(h1)

    #     dfs(root)
    #     return diameter
        




        