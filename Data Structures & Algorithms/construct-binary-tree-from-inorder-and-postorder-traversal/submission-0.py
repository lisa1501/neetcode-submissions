# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v:i for i, v in enumerate(inorder)}
        print(pos)
        pos_idx = len(postorder)-1
        def dfs(left, right):
            nonlocal pos_idx

            if left > right:
                return None

            root_val = postorder[pos_idx]
            pos_idx -= 1

            root = TreeNode(root_val)

            mid = pos[root_val]

            root.right = dfs(mid+1, right)
            root.left = dfs(left, mid-1)

            return root
        
        return dfs(0, len(inorder)-1)
        