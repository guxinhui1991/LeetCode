# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        if root.left:
            return self.inorderTraversal(root.left) + [root.val] +self.inorderTraversal(root.right)
        else:
            return [root.val] + self.inorderTraversal(root.right)


    def inorderTraversal_loop(self, root):

        cur_stack = []
        res = []

        if not root: return res

        cur = root
        while cur or cur_stack:
            if cur:
                cur_stack.append(cur)
                cur = cur.left
            else:
                cur = cur_stack.pop()
                res.append(cur.val)
                cur = cur.right

        return res


    def inorderTraversal(self, root):
        res = []
        cur_stack = []

        if not root: return root

        cur_stack.append(root)
        while cur_stack:
            cur_node = cur_stack[-1]

            if cur_node:
                cur_stack.pop()
                if cur_node.right: cur_stack.append(cur_node.right)





r1 = TreeNode(val=3, left = TreeNode(6), right = TreeNode(7))
l1 = TreeNode(val=2, left = TreeNode(4), right = TreeNode(5))
r=TreeNode(val=1, left = l1, right = r1)

Solution().inorderTraversal_loop(root=r)