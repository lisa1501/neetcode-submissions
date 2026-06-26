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

            rob_with_left_node, rob_without_left_node = dfs(node.left)
            rob_with_right_node, rob_without_right_node = dfs(node.right)

            rob_with_cur_node = node.val + rob_without_left_node + rob_without_right_node
            rob_without_cur_node = max(rob_with_left_node, rob_without_left_node) + max(rob_with_right_node, rob_without_right_node)

            return (rob_with_cur_node, rob_without_cur_node)

        return max(dfs(root))


        