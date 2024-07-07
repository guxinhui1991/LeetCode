# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def checkNode(self, node, max_V, min_V):
        if not node: return True
        if (node.val>=max_V) or (node.val<=min_V):
            return False
        return self.checkNode(node.left, node.val, min_V) and self.checkNode(node.right, max_V,node.val)

    # Recursive
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return
        import sys
        max_V = sys.maxsize
        min_V = -sys.maxsize - 1
        return self.checkNode(root,  max_V, min_V)

    # Iterative
    # Store all values in list
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        list_node = []
        def traversal(root):
            nonlocal list_node
            if not root: return

            if root.right:
                traversal(root.right)
            list_node.append(root)
            if root.left:
                traversal(root.left)
        traversal(root)
        for i in range(len(list_node) - 1):
            if list_node[i].val <= list_node[i + 1].val:
                return False

        return True

    # Recursive - In-order traversal
    # Only need to store the previous value

    def isValidBST3(self, root: Optional[TreeNode]) -> bool:
        prev = -float('inf')
        def helper(node):
            nonlocal prev
            if not node: return True
            l = r = True
            if node.left:
                l = helper(node.left)
            if node.val <= prev: return False
            prev = node.val
            if node.right:
                r = helper(node.right)
            return l and r


        return helper(root)

test1 = TreeNode(2)
test2 = TreeNode(2)
test3 = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().isValidBST1(test3))
print(Solution().isValidBST2(test3))