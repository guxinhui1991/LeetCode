# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        q = deque([root])
        f = False
        while q:
            l = len(q)
            cur = []
            for _ in range(l):
                n = q.popleft()
                cur.append(n)
                if n:
                    q.append(n.left)
                    q.append(n.right)

            for n in cur:
                if not n:
                    f = True
                else:
                    if f: return False

        return True