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

            if node.val > p.val and node.val > q.val:
                return helper(node.left)
            elif node.val < p.val and node.val < q.val:
                return helper(node.right)
            else:
                return node

        return helper(root)