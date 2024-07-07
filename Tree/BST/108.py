# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def generateNums(node):
            #res = []
            # stack = deque([node])
            # while stack:
            #     cur_node = stack.pop()
            #     if cur_node.right: stack.append(cur_node.right)
            #     if cur_node.left: stack.append(cur_node.left)
            #     res.append(cur_node.val)
            if not node: return []
            if not node.left and not node.right: return [node.val]
            l = generateNums(node.left)
            r=  generateNums(node.right)
            return l+[node.val] + r

        nums = generateNums(root)
        total_val = sum(nums)

        def helper(node):
            if not node: return
            idx = 0

            stack = [node]
            while stack:
                cur_node = stack.pop()
                if cur_node:
                    if cur_node.right: stack.append(cur_node.right)
                    stack.append(cur_node)
                    stack.append(None)
                    if cur_node.left: stack.append(cur_node.left)
                else:
                    cur_node = stack.pop()
                    cur_node.val = cur_node.val + total_val - nums[idx]
                    idx += 1

        helper(root)
        return root

l = TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3)))
r = TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8)))
root = TreeNode(4, l, r)

Solution().convertBST(root)