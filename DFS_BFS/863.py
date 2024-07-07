from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def convertToGraph(node, parent):
            nonlocal g
            if not node: return
            if parent: g[node].append(parent)
            if node.left:
                g[node].append(node.left)
                convertToGraph(node.left, node)
            if node.right:
                g[node].append(node.right)
                convertToGraph(node.right, node)

        g = defaultdict(list)
        convertToGraph(root, None)

        q = deque([target])
        vis = set()
        for _ in range(k):
            l = len(q)
            for _ in range(l):
                c = q.popleft()
                vis.add(c)
                for n in g[c]:
                    if n not in vis: q.append(n)

        return [i.val for i in q]