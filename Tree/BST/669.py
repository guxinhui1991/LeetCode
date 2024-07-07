# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root: return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # if not root.left and not root.right: return root

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root


test1 = TreeNode(3)
test2 = TreeNode(1)
test3 = TreeNode(2, test2, test1)
low = 3
high = 4
Solution().trimBST(test3, low, high)
Solution().trimBST2(test3, low, high)