# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # def isChild(self, root, target):
    #
    #     if not root: return False
    #     return self.isChild(root.left, target) or self.isChild(root.right, target) or root==target

    def lowestCommonAncestor_helper(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None

        self.ans = None
        def helper(root, p, q):

            # if not root: return False
            # if root == needle or root == q:
            #     return root

            if not root : return False
            l = r = None
            if root.left:
                l = helper(root.left, p, q)
            if root.right:
                r = helper(root.right,p, q)

            cur = root==p or root==q
            if (l and r) or (cur and l) or (cur and r):
                self.ans = root
                return

        helper(root, p, q)
        return self.ans

    # Without helper
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root==p or root ==q: return root


        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if (l and r): return root
        elif l: return l
        elif r: return r
        else: return None

