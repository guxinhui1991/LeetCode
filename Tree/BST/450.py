# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findLeftMostNode(self, node):
        if not node: return None

        while node.left:
            node = node.left
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root : return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right: return None
            elif root.left and not root.right: return root.left
            elif root.right and not root.left: return root.right
            elif root.left and root.right:
                cur = self.findLeftMostNode(root.right)
                cur.left = root.left
                root = root.right
                return root
        return root

root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
root = TreeNode(1, None, TreeNode(2))
Solution().deleteNode(root, 1)