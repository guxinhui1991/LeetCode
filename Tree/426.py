class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    ################################################
    #   Using additional stack
    ################################################

    def treeToDoublyList1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        q = []

        def dfs(node):
            nonlocal q
            if not node: return
            dfs(node.left)
            q.append(node)
            dfs(node.right)

        dfs(root)
        i, N = 0, len(q)
        while i < N:
            if i < N - 1: q[i].right = q[i + 1]
            if i > 0: q[i].left = q[i - 1]
            i += 1
        q[0].left = q[-1]
        q[-1].right = q[0]
        return q[0]


    def treeToDoublyList2(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root: return None

        def dfs(node):
            nonlocal first, last
            if not node: return
            dfs(node.left)

            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            dfs(node.right)

        first, last = None, None
        dfs(root)
        last.right, first.left = first, last

        return first