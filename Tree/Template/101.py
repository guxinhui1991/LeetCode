# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

####################################
#
#   Recursion Method
#
####################################
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(l, r):

            if not l and not r: return True
            elif (not l and r) or (not r and l): return False
            else:
                if l.val == r.val:
                    return helper(l.left, r.right) and helper(l.right, r.left)
                else:
                    return False

        return helper(root, root)

####################################
#
#   Iteration Method
#
####################################
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def testSymmetric(root):
            if not root: return True

            queue = []
            queue.append(root.left)
            queue.append(root.right)

            while (queue):
                lNode = queue.pop()
                rNode = queue.pop()
                if (not lNode and not rNode): continue

                if (not lNode or not rNode or lNode.val != rNode.val): return False

                queue.append(lNode.left)
                queue.append(rNode.right)
                queue.append(lNode.right)
                queue.append(rNode.left)

            return True

        return testSymmetric(root)


r1 = TreeNode(val=3, left=TreeNode(6), right=TreeNode(7))
l1 = TreeNode(val=2, left=TreeNode(3), right=TreeNode(4))
r = TreeNode(val=1, left=l1, right=r1)
