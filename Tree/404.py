# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        cur = 0
        def isLeaf(root):
            if not root: return False
            return not root.left and not root.right


        def helper(root, cur):
            if not root: return 0
            if isLeaf(root.left):
                return cur+root.left.val + helper(root.right, cur)
            return helper(root.left, cur) + helper(root.right, cur)

        return helper(root, cur)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().sumOfLeftLeaves(root))
