import sys
from typing import Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_sum = -sys.maxsize
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSumPartial(root):
            if not root: return 0
            # if not root.left and not root.right:
            #     if root.val > self.max_sum:
            #         self.max_sum = root.val
            #     return root.val

            # l, r = -sys.maxsize, -sys.maxsize
            # if root.left:
            #     l = max(0, maxPathSumPartial(root.left))
            # if root.right:
            #     r = maxPathSumPartial(root.right)

            # if root.val >= 0:
            #     if l + root.val > self.max_sum: self.max_sum = l + root.val
            #     if r + root.val > self.max_sum: self.max_sum = r + root.val
            #     if l + r + root.val > self.max_sum: self.max_sum = l + r + root.val
            #
            # else:
            #     if l > self.max_sum: self.max_sum = l
            #     if r > self.max_sum: self.max_sum = r

            # if root.val > self.max_sum: self.max_sum = root.val

            l = max(0, maxPathSumPartial(root.left))
            r = max(0, maxPathSumPartial(root.right))
            cur_max = l + r + root.val
            self.max_sum = max(self.max_sum , cur_max)
            return root.val + max(l, r)

        maxPathSumPartial(root)
        return self.max_sum


l1 = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None)
r1 = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))

l2= TreeNode(5, TreeNode(4, None,TreeNode(2, TreeNode(-4))))
root = TreeNode(5, l2)
root = TreeNode(-2, TreeNode(-1))
print(Solution().maxPathSum(root))