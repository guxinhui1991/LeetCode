# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Incorrect :
    #   2
    # 1   3
    #  4
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        res = []
        cur_level = 0
        stack = [root]
        cur_max = []
        while stack:
            cur_len = len(stack)
            cur_sum = 0
            for _ in range(cur_len):
                cur_node = stack.pop()
                cur_sum += cur_node.val
                if cur_node.left: stack.insert(0, cur_node.left)
                if cur_node.right: stack.insert(0, cur_node.right)
            res.append(cur_sum)
            if cur_level<2:
                cur_max.append(max(cur_sum, max(res, default=0)))
            else:
                cur_max.append(max(cur_sum + max(res[:cur_level - 1]), cur_max[cur_level-1]))
            cur_level += 1
        return cur_max[-1]



    def rob2(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            if not node: return [0, 0]

            l = traverse(node.left)
            r = traverse(node.right)

            v1 = node.val + l[1] + r[1]
            v2 = max(l[0], l[1]) + max(r[0], r[1])

            return [v1, v2]

        return max(traverse(root))


r = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode()))
r = TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3))))
r = TreeNode(3, TreeNode(2, None, TreeNode(4, TreeNode(1))))
print(Solution().rob2(r))


