"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def __init__(self):
        self.visited = {}

    def copyNode(self, oldNode):
        if oldNode:
            if oldNode in self.visited:
                return self.visited[oldNode]
            else:
                newNode = Node(oldNode.val)
                self.visited[oldNode] = newNode
                return newNode
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: return head
        curr_old = head
        curr_new = Node(head.val)
        head_new = curr_new
        self.visited[curr_old] = curr_new

        while curr_old:
            curr_new.next = self.copyNode(curr_old.next)
            curr_new.random = self.copyNode(curr_old.random)
            curr_old = curr_old.next
            curr_new = curr_new.next

        return head_new