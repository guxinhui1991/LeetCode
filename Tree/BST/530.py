# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = sys.maxsize

    # Compare left and right for each node --- Slow
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l_max =  -sys.maxsize-1
        r_min = sys.maxsize
        def getMaxVal(root):
            nonlocal l_max
            if not root: return
            if root.val > l_max: l_max = root.val
            getMaxVal(root.left)
            getMaxVal(root.right)
            return

        def getMinVal(root):
            nonlocal r_min
            if not root: return
            if root.val < r_min: r_min = root.val
            getMinVal(root.left)
            getMinVal(root.right)
            return

        if root.left: getMaxVal(root.left)
        if root.right: getMinVal(root.right)
        self.res = min(root.val - l_max, r_min - root.val, abs(self.res))
        self.getMinimumDifference(root.left)
        self.getMinimumDifference(root.right)
        return self.res

class Solution2:
    # In-order traversal -- Fast
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        p = -float('inf')
        res = 10 ** 5

        def DFS(node):
            nonlocal p, res
            if not node: return
            if node.left: DFS(node.left)
            res = min(res, node.val - p)
            p = node.val
            if node.right: DFS(node.right)

        DFS(root)
        return res

root = TreeNode(10, TreeNode(2, None, TreeNode(8)), TreeNode(14, TreeNode(13)))
print(Solution2().getMinimumDifference(root))
print(Solution().getMinimumDifference(root))