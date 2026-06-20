# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node): 
            # nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # res += 1+max(left, right)
            return 1 + max(left, right)
            # dfs(1) 
            # dfs(2) => l_dfs(null) =0 r__dfs(null) =0 => 1+max(0,0) = 1 res = 1
            # dfs(3) => dfs(4)
            # dfs(4)=> l_dfs(null) =0 r__dfs(null) =0 => 1+max(0,0) = 1 res = 1+1
            # dfs(3) => l_dfs(4) =1 r__dfs(null) =0 => 1+max(1,0) = 2 res = 1+1+2
            # dfs(1)=> l_dfs(2) =1 r__dfs(3) =2 => 1+max(1,2) = 3 res = 1+1+2+3

        return dfs(root)
        

        