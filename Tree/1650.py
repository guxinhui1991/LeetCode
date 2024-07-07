

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def checkChild(p, q):
            stack = [p]
            while stack:
                cur_len = len(stack)
                for _ in range(cur_len):
                    cur_node = stack.pop(0)
                    if cur_node == q: return True
                    if cur_node.left: stack.append(cur_node.left)
                    if cur_node.right: stack.append(cur_node.right)

            return False

        # check if b is child of a
        def checkChild_faster(a, b):
            while b.parent:
                if a == b:
                    return True
                b = b.parent
            return False

        def helper(p, q):
            if not p or not q: return None
            if checkChild(p, q): return p
            if checkChild(q, p): return q

            if p == q: return p

            return helper(p.parent, q.parent)

        return helper(p, q)


class Solution2:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        path_p = [p]
        while p.parent:
            path_p.append(p.parent)
            p = p.parent

        path_q = [q]
        while q.parent:
            path_q.append(q.parent)
            q = q.parent

        res = None
        idx = 0
        while idx < len(path_p) and idx < len(path_q) and path_p[::-1][idx] == path_q[::-1][idx]:
            res = path_p[::-1][idx]
            idx += 1

        return res

root = Node(3, Node(5))