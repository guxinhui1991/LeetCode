"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    ####################################
    # BFS
    ####################################
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        def helper(r):
            stack =[r]
            cur_level = 1
            while stack:
                cur_node = stack.pop()
                if cur_node.children:
                    for i in range(len(cur_node.children)):
                        stack.append(cur_node.children[i])
                    cur_level += 1
                else:
                    continue
            return cur_level

        return helper(root)


    ####################################
    # DFS
    ####################################
    def maxDepth_DFS(self, root: 'Node') -> int:

        res = 0

        def DFS(node, d):
            nonlocal res
            if not node: return
            res = max(res, d)

            arr = node.children
            for c in arr:
                d += 1
                DFS(c, d)
                d -= 1

        DFS(root, 1)
        return res


r = Node(1)
l1_1 = Node(3)
l1_2 = Node(2)
l1_3 = Node(4)
r.children = [l1_1, l1_2, l1_3]
print(Solution().maxDepth(r))