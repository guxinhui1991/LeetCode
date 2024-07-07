# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    ############################################
    #
    #   Iteration method
    #
    ############################################
    def maxDepth(self, root):
        if not root: return 0
        queue = [root]
        level = 0
        while (queue):
            size = len(queue)
            for i in range(size):
                tmpNode = queue.pop()
                if tmpNode.left:
                    queue.insert(0, tmpNode.left)
                if tmpNode.right:
                    queue.insert(0, tmpNode.right)
            level += 1
        return level

    ############################################
    #
    #   Recursion method - Post-order-traversal
    #
    ############################################
    def maxDepth_recursion(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            return 1 + max(l, r)

        return helper(root)

    ############################################
    #
    #   Recursion method - Pre-order-traversal
    #
    ############################################
    def maxDepth_recursion(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(node, d):
            nonlocal res
            if not node: return
            res = max(res, d)
            if node.left:
                d += 1
                helper(node.left, d)
                d -= 1
            if node.right:
                d += 1
                helper(node.right, d)
                d -= 1

        helper(root, 1)
        return res