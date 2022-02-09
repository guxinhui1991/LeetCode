# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = [[root.val]]

        level = []
        if root.left:
            level.append(root.left)
        if root.right:
            level.append(root.right)

        while level:
            res.append([i.val for i in level])
            newLevel = []
            for i in level:
                if i.left:
                    newLevel.append(i.left)
                if i.right:
                    newLevel.append(i.right)
            level = newLevel

        return res

    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []

        level = [root]

        while level:
            res.append([i.val for i in level])
            newLevel = []
            for i in level:
                if i.left:
                    newLevel.append(i.left)
                if i.right:
                    newLevel.append(i.right)
            level = newLevel

        return res



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().levelOrder2(root))