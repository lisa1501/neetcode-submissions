# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            if not node:
                return (0,0)

            skip_node_left, with_node_left = dfs(node.left)
            skip_node_right, with_node_right = dfs(node.right)

            skip_node = max(skip_node_left, with_node_left) + max(skip_node_right, with_node_right)
            with_node = node.val + skip_node_left + skip_node_right
            
            return (skip_node, with_node)
            
        return max(dfs(root))
