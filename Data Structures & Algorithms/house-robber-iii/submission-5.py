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

            with_left_node, skip_left_node = dfs(node.left)
            with_right_node, skip_right_node = dfs(node.right)

            with_node = skip_left_node + skip_right_node + node.val
            skip_node = max(with_left_node, skip_left_node) + max( with_right_node, skip_right_node)
            return (with_node, skip_node)

        return max(dfs(root))

    # def maxAverage(self, root: Optional[TreeNode]) -> int:
    #     ans = float('-inf')
    
    #     def dfs(node):

    #         nonlocal ans

    #         if not node:
    #             return (0, 0)

    #         left_sum_nodes, left_count_nodes = dfs(node.left)
    #         right_sum_nodes, right_count_nodes = dfs(node.right)

    #         sum_nodes += node.val + left_sum_nodes + right_sum_nodes
    #         count_nodes += 1 + left_count_nodes + right_count_nodes

    #         ans = max(ans, sum_nodes/count_nodes)

    #         return (sum_nodes, count_nodes)

    #     dfs(root)
    #     return ans

    
        
        