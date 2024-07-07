# Definition for a binary tree node.

from collections import deque
import sys

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        # leaf node
        if not root.left and not root.right: return 1

        l_depth, r_depth = sys.maxsize, sys.maxsize
        if root.left:
            l_depth = self.minDepth(root.left)
        if root.right:
            r_depth = self.minDepth(root.right)

        return min(l_depth, r_depth) + 1


    def minDepth2(self, root):
        def helper(root):
            stack = deque([root])
            cur_min = 0
            while stack:
                cur_min +=1
                for _ in range(len(stack)):
                    cur_node = stack.popleft()
                    if not cur_node.left and not cur_node.right:
                        return cur_min
                    else:
                        if cur_node.left: stack.append(cur_node.left)
                        if cur_node.right: stack.append(cur_node.right)
            return cur_min

        return helper(root)


root = TreeNode(9)
root.left = TreeNode(-3)
root.right = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(-6)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(-5)
root.right.right = TreeNode(0)
print(Solution().minDepth(root))
print(Solution().minDepth2(root))