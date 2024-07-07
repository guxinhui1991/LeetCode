# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
##########################################################
#
# Iterative
#
##########################################################
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        if not root: return res

        cur_stack = [(root, 0)]
        total_sum = 0
        while cur_stack:
            cur_node, cur_sum = cur_stack.pop()
            cur_sum = cur_sum * 10 + cur_node.val
            if not cur_node.left and not cur_node.right:
                total_sum += cur_sum

            else:
                if cur_node.left:
                    cur_stack.append((cur_node.left, cur_sum))
                if cur_node.right:
                    cur_stack.append((cur_node.right, cur_sum))

        return total_sum


##########################################################
#
# Recursive
#
##########################################################
class Solution2:
    def sumNumbers(self, root):
        tmp = root
        res = self.getList(tmp)
        return sum(int(i) for i in res)

    def getList(self, root):
        if not root: return []
        if not root.left and not root.right: return str(root.val)

        children_nodes_left = self.getList(root.left)
        children_nodes_right = self.getList(root.right)

        res = []
        for i in children_nodes_left:
            res.append(str(root.val) + i)

        for i in children_nodes_right:
            res.append(str(root.val) + i)

        return res

r1 = TreeNode(val=3, left=TreeNode(6), right=TreeNode(7))
l1 = TreeNode(val=2, left=TreeNode(3), right=TreeNode(4))
r = TreeNode(val=1, left=l1, right=r1)
print(Solution2().sumNumbers(r))
print(Solution().sumNumbers(r))
