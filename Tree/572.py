# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def checkTree(node1, node2):
            if not node1 and not node2:
                return True
            elif (node2 and not node1) or (node1 and not node2):
                return False
            else:
                if node1.val == node2.val:
                    return checkTree(node1.left, node2.left) and checkTree(node1.right, node2.right)
                else:
                    return False

        def helper(node, subRoot):
            nonlocal res
            if not node: return
            if checkTree(node, subRoot):
                res = True
                return
            helper(node.left, subRoot)
            helper(node.right, subRoot)
            return

        helper(root, subRoot)
        return res