# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # Recursion
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def invertTree_recursion(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # BFS - Level Order traversal - complex version
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def invertTree_bfs(self, root):
        import queue
        cur_level = collections.deque([root])

        while cur_level:
            cur_level_len = len(cur_level)

            for _ in range(cur_level_len):
                node = cur_level.popleft()
                if node.left: cur_level.append(node.left)
                if node.left: cur_level.append(node.right)


                tmp = node.left
                node.left = node.right
                node.right = tmp

        return root

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    # BFS - simpler version
    # DFS - preOrder traversal
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def invertTree_preorder(self, root):
        cur_stack = [root]
        while cur_stack:
            cur_node = cur_stack[-1]
            cur_stack.pop()

            if cur_node:
                if cur_node.right: cur_stack.append(cur_node.right)
                if cur_node.left: cur_stack.append(cur_node.left)

                cur_stack.append(cur_node)
                cur_stack.append(None)


            else:
                cur_node = cur_stack.pop()
                cur_node.left, cur_node.right = cur_node.right, cur_node.left

        return root

    def invertTree_preorder_simple(self, root):
        def BFS(node):
            if not node: return
            q = collections.deque([node])

            while q:
                l = len(q)
                for _ in range(l):
                    n = q.popleft()
                    if n.left: q.append(n.left)
                    if n.right: q.append(n.right)

                    n.left, n.right = n.right, n.left

        def DFS(node):
            if not node: return
            q = [node]

            while q:
                n = q.pop()
                n.left, n.right = n.right, n.left
                if n.right: q.append(n.right)
                if n.left: q.append(n.left)

        # DFS(root)
        BFS(root)

        return root

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    Solution().invertTree_preorder(root)
    inOrder(root)