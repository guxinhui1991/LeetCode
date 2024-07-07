from typing import Optional
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution_DFS:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return
        if node in self.visited: return self.visited[node]

        cur_new = Node(node.val, [])
        self.visited[node] = cur_new
        if node.neighbors:
            cur_new.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return cur_new


class Solution_BFS(object):

    def cloneGraph(self, node):
        if not node: return node

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])

        return visited[node]