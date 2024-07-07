# Definition for a binary tree node.
from typing import Optional, List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        cur_level = [root]
        res_tree = []
        while cur_level:
            res_level = []
            next_level = []
            len_level = len(cur_level)

            for _ in range(len_level):
                cur_node = cur_level.pop()
                if cur_node.left: next_level.append(cur_node.left)
                if cur_node.right: next_level.append(cur_node.right)
                res_level.append(cur_node.val)

            res_tree.append(res_level)
            cur_level = next_level[::-1]

        return res_tree[::-1]


root = TreeNode(9)
root.left = TreeNode(-3)
root.right = TreeNode(2)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(-6)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(-5)
root.right.right = TreeNode(0)
import timeit

start = timeit.default_timer()
print(Solution().levelOrderBottom(root))
stop = timeit.default_timer()
print('Time: ', stop - start)
