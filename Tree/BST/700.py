# Definition for a binary tree node.

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None

        stack = deque([root])
        while stack:

            for _ in range(len(stack)):
                cur_node = stack.popleft()
                if cur_node.val == val: return cur_node

                if cur_node.left: stack.append(cur_node.left)
                if cur_node.right: stack.append(cur_node.right)

        return None

class Solution2(object):
    def searchBST(self, root, val):
        if not root: return
        if root.val == val:
            return root
        elif  val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)