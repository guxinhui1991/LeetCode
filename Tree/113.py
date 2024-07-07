# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.ans =[]

    def findResult(self, root, targetSum, curr):
        if not root: return

        if (targetSum == 0 and not root.left and not root.right):
            self.ans.append(curr)
            return

        res = []
        # if root.left:
        #     cur_cpy = curr.copy()
        #     cur_cpy.append(root.left.val)
        #     self.findResult(root.left, targetSum-root.left.val, cur_cpy)
        # if root.right:
        #     cur_cpy = curr.copy()
        #     cur_cpy.append(root.right.val)
        #     self.findResult(root.right, targetSum-root.right.val, cur_cpy)

        if root.left:
            self.findResult(root.left, targetSum-root.left.val, curr+[root.left.val])
        if root.right:
            self.findResult(root.right, targetSum-root.right.val, curr+[root.right.val])
        return

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        self.findResult(root, targetSum - root.val, [root.val])
        return self.ans

# Test 1
t_3 = TreeNode(-3)

t_2 = TreeNode(-2, None, t_3)
print(Solution().pathSum(t_2, -5))

# Test 2
t_7 = TreeNode(7)
t_2 = TreeNode(2)
t_5 = TreeNode(5)
t_1 = TreeNode(1)

t_11 = TreeNode(11, t_7, t_2)
t_4 = TreeNode(4, t_5, t_1)
t_13 = TreeNode(13)

t_4_2 =  TreeNode(4, t_11)
t_8 = TreeNode(8, t_13, t_4)

t_5 = TreeNode(5, t_4_2, t_8)

print(Solution().pathSum(t_5, 22))