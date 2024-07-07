# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.path = []
    def findPaths(self, root, curr):
        if not root.left and not root.right:
            self.path.append(curr[:-2])
        # if root.left:
        #     cur_cpy = str(curr)
        #     cur_cpy += str(root.left.val) + "->"
        #     self.findPaths(root.left, cur_cpy)
        #
        # if root.right:
        #     cur_cpy = str(curr)
        #     cur_cpy += str(root.right.val) + "->"
        #     self.findPaths(root.right, cur_cpy)
        if root.left: self.findPaths(root.left, curr + str(root.left.val) + "->")
        if root.right: self.findPaths(root.right, curr + str(root.right.val) + "->")
        return

    def binaryTreePaths(self, root):
        if not root: return
        self.findPaths(root, str(root.val) + "->")
        return self.path

    def binaryTreePaths2(self, root):
        if not root: return
        def treeNodesList(root, curr):
            if not root:
                return []
            if not root.left and not root.right:
                for i in curr:
                    i.append(root)
                return curr

            res_l , res_r = [], []
            if root.left:
                res_l = treeNodesList(root.left, [[root]])

            if root.right:
                res_r = treeNodesList(root.right, [[root]])

            return [i + j for i in curr for j in res_l + res_r]

        path_list = treeNodesList(root, [[]])
        res = []
        for path in path_list:
            res.append('->'.join([str(i.val) for i in path]))
        return res




root = TreeNode(1)
root.left = TreeNode(2)
#root.left.right = TreeNode(5)
root.right = TreeNode(3)


#print(Solution().binaryTreePaths(root))
print(Solution().binaryTreePaths2(root))
