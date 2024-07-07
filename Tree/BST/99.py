# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################
# Recursive method
##############################################
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.cur = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def find(r):
            if not r: return None

            find(r.left)
            if(self.cur and self.cur.val >= r.val):
                if not self.first: self.first = self.cur
                self.second = r
            self.cur = r
            find(r.right)
            return r

        find(root)
        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp

        return root

##############################################
# Iterative method
##############################################
class Solution2:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        stack = []

        def helper(node):
            nonlocal stack
            if not node: return []
            return helper(node.left) + [node] + helper(node.right)
        stack = helper(root)

        # def helper2(node):
        #     nonlocal stack
        #     if not node: return []
        #     if node.left: stack += helper(node.left)
        #     stack += [node]
        #     if node.right: stack += helper(node.right)
        #     return stack
        # helper2(root)

        val_sorted = sorted(n.val for n in stack)

        for i in range(len(stack)):
            stack[i].val = val_sorted[i]
        return


l1 = TreeNode(val=3, right = TreeNode(2))
r=TreeNode(val=1, left = l1)
Solution().recoverTree(r)
Solution2().recoverTree(r)