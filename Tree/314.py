# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return

        res = {}
        res[0] = [root.val]
        def helper(node, cur_index):
            nonlocal res
            if not node: return
            #res[cur_index] = res.get(cur_index, []) + [node.val]

            # if node.left:
            #     res[cur_index-1] = res.get(cur_index-1, []) + [node.left.val]
            # if node.right:
            #     res[cur_index+1] = res.get(cur_index+1, []) + [node.right.val]
            # if node.left:
            #     helper(node.left, cur_index-1)
            # if node.right:
            #     helper(node.right, cur_index+1)

            stack = [(node, cur_index)]
            while stack:
                cur_len = len(stack)
                for _ in range(cur_len):
                    cur_node, cur_node_index = stack.pop(0)
                    if cur_node.left:
                        res[cur_node_index-1] = res.get(cur_node_index-1, []) + [cur_node.left.val]
                    if cur_node.right:
                        res[cur_node_index+1] = res.get(cur_node_index+1, []) + [cur_node.right.val]
                    if cur_node.left:
                        stack.append((cur_node.left, cur_node_index-1))
                    if cur_node.right:
                        stack.append((cur_node.right, cur_node_index+1))


        helper(root, 0)

        key_sorted = sorted(res.keys())
        output =[res[k] for k in key_sorted]

        return output

# Jan 2024 - redo refine
class Solution2:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        res = {}

        def helper(node):
            nonlocal res
            stack = [(node, 0)]

            while stack:
                cur_len = len(stack)
                for _ in range(cur_len):
                    cur_node, cur_idx = stack.pop(0)
                    res[cur_idx] = res.get(cur_idx, []) + [cur_node.val]
                    if cur_node.left: stack.append((cur_node.left, cur_idx - 1))
                    if cur_node.right: stack.append((cur_node.right, cur_idx + 1))

            return

        helper(root)
        return [res[k] for k in sorted(res.keys())]



root = TreeNode(3, TreeNode(9,  TreeNode(4), TreeNode(0, None, TreeNode(2))), TreeNode(8,  TreeNode(1, TreeNode(5)), TreeNode(7)))
test = TreeNode(8,  TreeNode(1, None, TreeNode(2)), TreeNode(7))
print(Solution().verticalOrder(test))
print(Solution().verticalOrder(root))