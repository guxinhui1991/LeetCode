# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = -sys.maxsize

        def helper(node):
            nonlocal res
            if not node.left and not node.right:
                res = max(res, node.val)
                return node.val, 1

            cur_sum = node.val
            num_nodes = 1
            if node.left:
                l_sum, l_nodes = helper(node.left)
                num_nodes += l_nodes
                cur_sum += l_sum
            if node.right:
                r_sum, r_nodes = helper(node.right)
                num_nodes += r_nodes
                cur_sum += r_sum

            if num_nodes: res = max(res, cur_sum / num_nodes)
            return cur_sum, num_nodes

        helper(root)
        return res
