# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 0
        q = [(root, 0)]

        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            l = len(q)
            for _ in range(l):
                c, i = q.pop(0)
                if c.left: q.append((c.left, 2 * i))
                if c.right: q.append((c.right, 2 * i + 1))

        return res