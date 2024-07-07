# Definition for a binary tree node.
from typing import Optional, List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        cur_stack = []
        res = []

        if not root: return res

        cur_stack.append(root)
        while cur_stack:
            cur_node = cur_stack.pop()
            res.append(cur_node.val)
            if cur_node.left: cur_stack.append(cur_node.left)
            if cur_node.right: cur_stack.append(cur_node.right)

        return res[::-1]