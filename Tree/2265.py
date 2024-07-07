# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        res = 0

        def helper(node):
            nonlocal res
            if not node: return 0, 0

            l, nl = helper(node.left)
            r, nr = helper(node.right)

            if (l + r + node.val) // (nl + nr + 1) == node.val:
                res += 1

            return (l + r + node.val), nl + nr + 1

        helper(root)
        return res
