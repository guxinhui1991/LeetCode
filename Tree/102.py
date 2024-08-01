class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        if not root: return []

        level = []
        level.append(root)
        res = []
        while level:
            res.append([i.val for i in level])
            for _ in range(len(level)):
                cur_node = level.pop(0)
                if cur_node.left:
                    level.append(cur_node.left)
                if cur_node.right:
                    level.append(cur_node.right)
        return res


    def levelOrder2(self, root):
        res_arr = []

        def dfs(node, level, res):
            if not node: return
            if len(res) == level: res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)
            return res

        return dfs(root, 0, res_arr)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(6)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
import timeit

start = timeit.default_timer()
print(Solution().levelOrder(root))
stop = timeit.default_timer()
print('Time: ', stop - start)


start = timeit.default_timer()
print(Solution().levelOrder2(root))
stop = timeit.default_timer()
print('Time: ', stop - start)
