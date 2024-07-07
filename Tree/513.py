# Definition for a binary tree node.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ########################################################################
    #
    #   Level order traversal
    #
    ########################################################################

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = deque([root])
        max_depth = 1
        while stack:
            cur_vals = [i.val for i in stack]
            for _ in range(len(stack)):
                cur_node = stack.popleft()
                if (cur_node.left): stack.append(cur_node.left)
                if (cur_node.right): stack.append(cur_node.right)

            max_depth += 1

        return cur_vals[0]


    ########################################################################
    #
    #   Pre-order traversal
    #
    ########################################################################



    def findBottomLeftValue_DFS(self, root: Optional[TreeNode]) -> int:
        res = 0
        depth = -1

        def DFS(node, d):
            nonlocal res, depth
            if not node: return
            if d>depth:
                depth = d
                res = node.val
            DFS(node.left, d+1)
            DFS(node.right, d+1)


        DFS(root, 1)
        return res

