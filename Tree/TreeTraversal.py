# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
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
                cur_stack.append(cur_node)
                cur_stack.append(None)
                if cur_node.left: cur_stack.append(cur_node.left)
            else:
                cur_stack.pop()
                cur_node = cur_stack[-1]
                cur_stack.pop()
                res.append(cur_node.val)


        return res

    def preorderTraversal(self, root):
        res = []
        cur_stack = []

        if not root: return root

        cur_stack.append(root)
        while cur_stack:
            cur_node = cur_stack[-1]

            if cur_node:
                cur_stack.pop()
                if cur_node.right: cur_stack.append(cur_node.right)
                if cur_node.left: cur_stack.append(cur_node.left)
                cur_stack.append(cur_node)
                cur_stack.append(None)

            else:
                cur_stack.pop()
                cur_node = cur_stack[-1]
                cur_stack.pop()
                res.append(cur_node.val)


        return res

    def postorderTraversal(self, root):
        res = []
        cur_stack = []

        if not root: return root

        cur_stack.append(root)
        while cur_stack:
            cur_node = cur_stack[-1]

            if cur_node:
                cur_stack.pop()
                if cur_node.left: cur_stack.append(cur_node.left)
                if cur_node.right: cur_stack.append(cur_node.right)
                cur_stack.append(cur_node)
                cur_stack.append(None)

            else:
                cur_stack.pop()
                cur_node = cur_stack[-1]
                cur_stack.pop()
                res.append(cur_node.val)

        return res[::-1]


r1 = TreeNode(val=3, left = TreeNode(6), right = TreeNode(7))
l1 = TreeNode(val=2, left = TreeNode(4), right = TreeNode(5))
r=TreeNode(val=1, left = l1, right = r1)

print(Solution().preorderTraversal(root=r))
print(Solution().inorderTraversal(root=r))
print(Solution().postorderTraversal(root=r))