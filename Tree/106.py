from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursion 1
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder: return
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])

        return root

    # Recursion 2
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_dic = {v:i for i,v in enumerate(inorder)}
        def helper(l, r):
            if l > r: return
            v = postorder.pop()
            i = idx_dic[v]
            root = TreeNode(v)
            root.right = helper(i+1, r)
            root.left = helper(l, i-1)
            return root
        return helper(0, len(inorder)-1)



Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])