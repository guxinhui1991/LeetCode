# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def helper(node):
            if not node: return None, 0

            l, d_l = helper(node.left)
            r, d_r = helper(node.right)

            if d_l > d_r: return l, d_l + 1
            elif d_r > d_l: return r, d_r + 1
            else: return node, d_l + 1

        return helper(root)[0]