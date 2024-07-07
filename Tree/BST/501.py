# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cur_stack = []
        res = {}
        cur_stack.append(root)

        while cur_stack:
            cur_node= cur_stack.pop()
            res[cur_node.val] = res.get(cur_node.val, 0) + 1

            if cur_node.left: cur_stack.append(cur_node.left)
            if cur_node.right: cur_stack.append(cur_node.right)

        max_value = max(res.values())
        return [key for key, value in res.items() if value == max_value]




r1 = TreeNode(val=2, left = TreeNode(2))
#r1 = TreeNode(val=3, left = TreeNode(6), right = TreeNode(7))
#l1 = TreeNode(val=2, left = TreeNode(4), right = TreeNode(5))
r=TreeNode(val=1, right = r1)