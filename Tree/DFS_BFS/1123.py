from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node, d):
            if not node: return node, 0
            l, l_d = helper(node.left, d + 1)
            r, r_d = helper(node.right, d + 1)

            if l_d > r_d:
                return l, l_d + 1
            elif l_d < r_d:
                return r, r_d + 1
            else:
                return node, l_d + 1

        return helper(root, 0)[0]