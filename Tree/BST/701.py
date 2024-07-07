
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)

        cur_node = root
        prev_node = None
        while cur_node:
            if val > cur_node.val:
                prev_node = cur_node
                cur_node = cur_node.right
                continue

            if val < cur_node.val:
                prev_node = cur_node
                cur_node = cur_node.left
                continue
        if val > prev_node.val:
            prev_node.right = TreeNode(val)
        else:
            prev_node.left = TreeNode(val)

        return root

root= TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
Solution().insertIntoBST(root, 8)