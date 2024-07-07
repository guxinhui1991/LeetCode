# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    ##########################################
    #   Dec 2023 -- First loop explicit
    ##########################################
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(val, arr_l, arr_r) -> TreeNode:

            if not arr_l and not arr_r:
                return TreeNode(val)
            else:
                root = TreeNode(val)
                if arr_l:
                    idx = arr_l.index(max(arr_l))
                    root.left = helper(arr_l[idx], arr_l[:idx], arr_l[idx+1:])
                if arr_r:
                    idx = arr_r.index(max(arr_r))
                    root.right = helper(arr_r[idx], arr_r[:idx], arr_r[idx+1:])


                return root

        idx = nums.index(max(nums))
        root = helper(nums[idx], nums[:idx], nums[idx+1:])
        return root


    ##########################################
    #   Jan 2024 - cleaner recusion
    ##########################################
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        v = max(nums)
        i = nums.index(v)

        root = TreeNode(v)
        root.left = self.constructMaximumBinaryTree(nums[:i])
        root.right = self.constructMaximumBinaryTree(nums[i + 1:])

        return root
