#Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = 0

    def getMaxDepth(self, root):
        if not root: return 0
        cur_depth = 0
        stack = deque([root])
        while stack:
            for _ in range(len(stack)):
                cur_node = stack.popleft()
                if cur_node.right: stack.append(cur_node.right)
                if cur_node.left: stack.append(cur_node.left)
            cur_depth += 1

        return cur_depth

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        diameter = self.getMaxDepth(root.left) + self.getMaxDepth(root.right)
        if diameter > self.res:
            self.res = diameter

        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return self.res

    def diameterOfBinaryTree_DFS(self, root: Optional[TreeNode]) -> int:

        res = 0

        def helper(node):
            nonlocal res
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            res = max(res, l + r)
            return max(l, r) + 1

        helper(root)
        return res


l = TreeNode(2, TreeNode(4), TreeNode(5))
root = TreeNode(1, l, TreeNode(3))
print(Solution().diameterOfBinaryTree(root))