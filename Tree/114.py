# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __int__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]
        while stack:
            cur_node = stack.pop()
            if cur_node.right: stack.append(cur_node.right)
            if cur_node.left: stack.append(cur_node.left)

            if stack: cur_node.right = stack[-1]
            cur_node.left = None

        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
Solution().flatten(root)

tmp = root
while tmp:
    print(tmp.val)
    tmp = tmp.right

