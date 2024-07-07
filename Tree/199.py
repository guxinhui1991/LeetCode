# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def helper(node):
            nonlocal res
            if not node: return
            stack = [node]
            while stack:
                cur_len = len(stack)
                cur_node = stack[0]
                for _ in range(cur_len):
                    cur_node = stack.pop(0)
                    if cur_node.left: stack.append(cur_node.left)
                    if cur_node.right: stack.append(cur_node.right)

                res.append(cur_node.val)
            return

        helper(root)
        return res