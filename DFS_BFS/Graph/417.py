from collections import deque
from typing import List


# DFS Solution
class Solution_DFS:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        N, M = len(h), len(h[0])
        ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        def DFS(x, y, vis):
            nonlocal N, M, res_P, res_A
            vis.add((x, y))
            cur_h = h[x][y]
            for d in ds:
                next_x, next_y = x + d[0], y + d[1]
                if 0 <= next_x < N and 0 <= next_y < M and h[next_x][next_y] >= cur_h and (next_x,next_y) not in vis:
                    DFS(next_x, next_y, vis)

        start_P, start_A = [], []
        res_P, res_A = set(), set()
        for i in range(N):
            start_P.append((i, 0))
            start_A.append((i, M-1))

        for i in range(M):
            start_P.append((0, i))
            start_A.append((N-1, i))


        for x,y in start_P: DFS(x, y, res_P)
        for x,y in start_A: DFS(x, y, res_A)
        return res_P & res_A

# BFS Solution
class Solution_BFS:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        N, M = len(h), len(h[0])
        ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def BFS(q):
            nonlocal N, M
            res = set()

            while q:
                x, y = q.popleft()
                res.add((x, y))
                cur_h = h[x][y]
                for d in ds:
                    next_x, next_y = x + d[0], y + d[1]
                    if 0 <= next_x < N and 0 <= next_y < M and h[next_x][next_y] >= cur_h and (next_x,next_y) not in res:
                        q.append((next_x, next_y))
            return res

        start_P, start_A = deque([]), deque([])
        for i in range(N):
            start_P.append((i, 0))
            start_A.append((i, M-1))

        for i in range(M):
            start_P.append((0, i))
            start_A.append((N-1, i))


        res_P = BFS(start_P)
        res_A = BFS(start_A)

        return res_P & res_A


Solution_DFS().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])