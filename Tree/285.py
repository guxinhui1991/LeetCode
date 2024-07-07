# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root: return

        res = None
        cur = sys.maxsize

        def helper(node):
            nonlocal p, res, cur
            if not node: return

            if node.val <= p.val:
                helper(node.right)
            elif node.val > p.val:
                if node.val - p.val < cur:
                    cur = node.val - p.val
                    res = node
                helper(node.left)

        helper(root)
        return res


    def inorderSuccessor_DFS(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        last = None

        def DFS(node):
            nonlocal last, p
            if not node: return
            if p.val==node.val: return last
            elif p.val < node.val:
                last = node
                return DFS(node.left)
            elif p.val > node.val:
                return DFS(node.right)

        return DFS(root)



