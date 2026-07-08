# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # Search for the key.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # Found the key.
        else:
            # case 1 — Leaf
            # case 2 — One Child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # case 3 -  has two children
            # Find the smallest node.
            cur = root.right
            while cur.left:
                cur = cur.left
            # updated deleted node(key) value 
            root.val = cur.val
            # remove 
            root.right = self.deleteNode(root.right, root.val)
        return root
        