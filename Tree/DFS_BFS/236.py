# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def helper(node):
            if not node: return
            c = node.val == p.val or node.val == q.val
            l = helper(node.left)
            r = helper(node.right)

            if (l and r) or (c and r) or (c and l):
                return node

            return l or r or c

        return helper(root)