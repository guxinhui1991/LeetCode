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


    def preorderTraversal_loop(self, root: Optional[TreeNode]) -> List[int]:
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

    def preorderTraversal_loop_uniform(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res

        cur_stack = [root]
        while cur_stack:
            cur = cur_stack[-1]
            if cur:
                cur_stack.pop()
                if cur.right: cur_stack.append(cur.right)
                if cur.left: cur_stack.append(cur.left)
                cur_stack.append(cur)
                cur_stack.append(None)
            else:
                cur_stack.pop()
                cur = cur_stack.pop()
                res.append(cur.val)

        return res