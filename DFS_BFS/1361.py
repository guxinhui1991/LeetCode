from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot():
            ch = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in ch: return i
            return -1

        root = findRoot()
        if root == -1: return False

        tree = set([root])
        vis = [False for _ in range(n)]
        vis[root] = True
        res = True

        def DFS(r):
            nonlocal vis, tree, res
            stack = [r]
            while stack:
                n_cur = stack.pop()
                l, r = leftChild[n_cur], rightChild[n_cur]

                for c in [l, r]:
                    if c != -1:
                        if vis[c]:
                            res = False
                            return
                        vis[c] = True
                        stack.append(c)
                        tree.add(c)
            res = True if len(tree) == n else False

        DFS(root)
        return res


print(Solution().validateBinaryTreeNodes(4, [1,-1,3,-1], [2,-1,-1,-1]))