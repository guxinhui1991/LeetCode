# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        res, cur = 1, 1

        def helper(node, val, cur):
            nonlocal res

            if not node: return

            if val != None and node.val == val + 1:
                cur += 1
            else:
                cur = 1
            res = max(res, cur)

            helper(node.left, node.val, cur)
            helper(node.right, node.val, cur)
            return

        helper(root, None, cur)
        return res
