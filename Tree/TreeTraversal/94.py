# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal_recursion(self, root):
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



    def inorderTraversal_loop_uniform(self, root):
        res = []
        if not root: return res

        cur_stack = [root]
        while cur_stack:
            cur = cur_stack[-1]
            if cur:
                cur_stack.pop()
                if cur.right: cur_stack.append(cur.right)
                cur_stack.append(cur)
                cur_stack.append(None)
                if cur.left: cur_stack.append(cur.left)
            else:
                cur_stack.pop()
                cur = cur_stack.pop()
                res.append(cur.val)

        return res


r1 = TreeNode(val=3, left = TreeNode(6), right = TreeNode(7))
l1 = TreeNode(val=2, left = TreeNode(4), right = TreeNode(5))
r=TreeNode(val=1, left = l1, right = r1)

Solution().inorderTraversal_loop(root=r)