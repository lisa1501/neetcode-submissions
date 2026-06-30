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
                return (0, 0)

            left_rob_node, left_skip_node = dfs(node.left)
            right_rob_node, right_skip_node = dfs(node.right)

            rob_node = node.val + left_skip_node + right_skip_node
            skip_node = max(left_rob_node, left_skip_node) + max(right_rob_node, right_skip_node)

            return (rob_node, skip_node)
            
        return max(dfs(root))
        
        