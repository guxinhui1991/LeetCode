from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


######################################################################
#
# O( nlog(n) )
#
######################################################################

class Solution(object):
    def height(self, root):
        if not root: return 0
        # if not root.left and not root.right: return 1
        return 1 + max(self.height(root.left),self.height(root.right))

    def isBalanced(self, root):

        if not root: return True
        l_h = self.height(root.left)
        r_h = self.height(root.right)

        return abs(l_h - r_h) <= 1 and (self.isBalanced(root.left)) and (self.isBalanced(root.right))

######################################################################
#
# O(n)
#
######################################################################

class Solution2(object):
    # def height(self, root, balanced):
    #     if not root:
    #         return 0, True
    #     if not root.left and not root.right:
    #         return 1, True
    #     l_h, l_balanced = self.height(root.left, balanced)
    #     r_h, r_balanced = self.height(root.right, balanced)
    #     if (abs(l_h - r_h) > 1 or not l_balanced or not r_balanced):
    #         return -1, False
    #     return max(l_h, r_h) + 1, True
    #
    # def isBalanced(self, root):
    #     if not root: return True
    #     return self.height(root, True)[1]

    def isBalancedHelper(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        l = self.isBalancedHelper(root.left)
        r = self.isBalancedHelper(root.right)
        if l == -1 or r == -1: return -1
        if abs(l - r) > 1: return -1
        return 1 + max(l, r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: return True
        return True if self.isBalancedHelper(root) > 0 else False

class Solution3:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root: return 0
            if not root.left and not root.right: return 1
            stack = deque([root])
            cur_height = 0
            while stack:
                for _ in range(len(stack)):
                    cur_node = stack.popleft()
                    if cur_node.right: stack.append(cur_node.right)
                    if cur_node.left: stack.append(cur_node.left)
                cur_height += 1

            return cur_height

        if not root: return True

        stack = deque([root])
        while stack:
            for _ in range(len(stack)):
                cur_node = stack.popleft()
                if (abs(height(cur_node.left) - height(cur_node.right)) > 1): return False
                if cur_node.right: stack.append(cur_node.right)
                if cur_node.left: stack.append(cur_node.left)

        return True


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

root.left.left = TreeNode(0)
root.left.left.left = TreeNode(2)

root.left.right = TreeNode(7)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(0)
root.left.right.right.left = TreeNode(7)

root.right.left = TreeNode(9)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(8)

print(Solution3().isBalanced(root))
print(Solution2().isBalanced(root))
