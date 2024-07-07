# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isCousins1(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # bfs

        res = []
        queue = [(root, None, 0)]

        while queue:
            node, parent, depth = queue.pop()

            if node.val == x:
                res.append((parent, depth))

            if node.val == y:
                res.append((parent, depth))

            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

        if len(res) == 2:
            node1, node2 = res[0], res[1]
            return node1[0]!=node2[0] and node1[1]==node2[1]

        return False

    def isCousins2(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # dfs

        res = []

        def dfs(root, parent, depth):
            if root.val == x:
                res.append((parent, depth))

            if root.val == y:
                res.append((parent, depth))

            if root.left: dfs(root.left, root, depth + 1)
            if root.right: dfs(root.right, root, depth + 1)

        dfs(root, None, 0)

        if len(res) == 2:
            node1, node2 = res[0], res[1]
            return node1[0]!=node2[0] and node1[1]==node2[1]

        return False