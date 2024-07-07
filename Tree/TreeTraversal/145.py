# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur_stack = []
        res = []

        if not root: return res

        cur_stack.append(root)
        while cur_stack:
            cur_node = cur_stack.pop()
            res.append(cur_node.val)
            if cur_node.right: cur_stack.append(cur_node.right)
            if cur_node.left: cur_stack.append(cur_node.left)

        return res