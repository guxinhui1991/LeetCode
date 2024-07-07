# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(l, r):
            if l == r: return [TreeNode(l)]
            if l > r: return [None]


            res = []
            for val in range(l, r+1):
                for l_tree in generate(l, val-1):
                    for r_tree in generate(val+1, r):
                        root = TreeNode(val, l_tree, r_tree)
                        res.append(root)

            return res


        return generate(1, n)

Solution().generateTrees(3)