from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    ####################################
    #   Apr 2023
    ####################################
    def connect1(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        queue = []
        res = []
        if not root: return

        if root.left != None and root.right != None:
            queue.append(root.right)
            queue.append(root.left)

        while (queue):
            size = len(queue)
            for i in range(size):
                tmpNode = queue.pop()
                if (i < size - 1):
                    tmpNode.next = queue[-1]
                if tmpNode.left: queue.insert(0, tmpNode.left)
                if tmpNode.right: queue.insert(0, tmpNode.right)

        return root

    ####################################
    #   Dec 2023
    ####################################
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def helper(node):
            if not node: return
            q = deque([node])
            while q:
                cur_len = len(q)
                # for _ in range(cur_len - 1):
                #     n = q.popleft()
                #     n.next = q[0]
                #     if n.left: q.append(n.left)
                #     if n.right: q.append(n.right)
                # n = q.popleft()
                # if n.left: q.append(n.left)
                # if n.right: q.append(n.right)
                for i in range(cur_len):
                    n = q.popleft()
                    if i < cur_len-1: n.next = q[0]
                    if n.left: q.append(n.left)
                    if n.right: q.append(n.right)
        helper(root)
        return root