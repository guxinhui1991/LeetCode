# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root: return targetSum == 0

        if not root.left and not root.right:
            return root.val == targetSum

        l, r = False, False
        if root.left:
            l = self.hasPathSum(root.left, targetSum - root.val)

        if root.right:
            r = self.hasPathSum(root.right, targetSum - root.val)

        return l or r


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

print(Solution().hasPathSum(root, 22))