# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> list:
        self.res = 0

        def dfs(node) -> list:
            if not node: return []
            if not node.left and not node.right: return [1]

            left_list = dfs(node.left)
            right_list = dfs(node.right)
            self.res += sum(l + r <= distance for l in left_list for r in right_list)
            return [1 + item for item in left_list + right_list]

        dfs(root)
        return self.res



print(Solution().countPairs(root = TreeNode([7,1,4,6,None,5,3,None,None,None,None,None,2]), distance=1))
print(TreeNode([7,1,4,6,None,5,3,None,None,None,None,None,2]).left)
