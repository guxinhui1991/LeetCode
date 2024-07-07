from collections import deque
from typing import List


class Solution_DFS:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:
        d = [[] for _ in range(N)]
        for p in pre:
            d[p[1]] += [p[0]]

        # Check if cycle exists in graph
        def DFS(n, cur):
            nonlocal visited
            # if n in current path, that means a cycle is found - return True
            if cur[n]: return True

            # if n in already visited, that means the node doesn't form a cycle in the child tree
            if visited[n]: return False

            cur[n] = True
            for j in d[n]:
                if DFS(j, cur): return True
            cur[n] = False

            ## for all child nodes, there are no cycle so mark as True
            visited[n] = True
            return False

        #   Call DFS method
        #   visited - nodes that has been visited
        #   cur - nodes in current path
        visited = [False for _ in range(N)]
        cur = [False for _ in range(N)]
        for i in range(N):
            if DFS(i, cur): return False
            visited[i] = True
        return True

class Solution_BFS:
    def canFinish(self, N: int, pre: List[List[int]]) -> bool:

        deg = [0 for _ in range(N)]
        d = [[] for _ in range(N)]
        for p in pre:
            d[p[1]].append(p[0])
            deg[p[0]] += 1

        q = deque([])
        for i in range(N):
            if deg[i] == 0: q.append(i)


        while q:
            t = q.popleft()
            for j in d[t]:
                deg[j] -= 1
                if deg[j] == 0 : q.append(j)

        # return True if all(i==0 for i in ind) else False
        return False if any(deg) else True


print(Solution_DFS().canFinish(2, [[0,1]]))
print(Solution_DFS().canFinish(2, [[1,0],[0,1]]))
print(Solution_DFS().canFinish(3, [[1,0],[2,1],[2,0]]))


print(Solution_BFS().canFinish(2, [[0,1]]))
print(Solution_BFS().canFinish(2, [[1,0],[0,1]]))