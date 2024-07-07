from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ######################################################
    #   Iterative Method
    ######################################################
    def countNodes_iterative(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = deque([root])
        count = 0
        while stack:
            count += len(stack)
            for _ in range(len(stack)):
                cur_node = stack.popleft()
                if cur_node.left: stack.append(cur_node.left)
                if cur_node.right: stack.append(cur_node.right)
        return count

    ######################################################
    #   Recusion Method
    ######################################################
    def countNodes_recusion(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node: return 0
            l, r = 1, 1
            cur_l, cur_r = node.left, node.right
            while cur_l:
                l += 1
                cur_l = cur_l.left
            while cur_r:
                r += 1
                cur_r = cur_r.right

            if l == r: return 2 ** l - 1
            else: return 1 + helper(node.left) + helper(node.right)

        return helper(root)

    ######################################################
    #   Recusion Method
    #   O(log(n) * log(n))
    #
    ######################################################
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(node):
            if not node: return 0
            return 1 + getDepth(node.left)

        def helper(node):
            if not node: return 0
            l = getDepth(node.left)
            r = getDepth(node.right)
            if l == r: return 2**l + helper(node.right)
            else:
                return helper(node.left) + 2**r

        return helper(root)