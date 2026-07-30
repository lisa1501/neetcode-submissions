# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root, 0)])
        while q:
            node, num = q.popleft()
            num = num * 10 + node.val

            if not node.left and not node.right:
                res += num
                continue

            if node.left:
                q.append((node.left, num))

            if node.right:
                q.append((node.right, num))
        return res