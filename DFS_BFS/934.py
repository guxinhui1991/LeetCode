from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        N = len(grid)
        dir = [(0,1),(0,-1),(1,0),(-1,0)]

        x, y = -1, -1
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    x, y = i, j
                    break

        def DFS(i, j):
            nonlocal nodes_start
            nodes_start.append((i, j))
            grid[i][j] = 2
            for d in dir:
                next_x, next_y = i + d[0], j +d[1]
                if 0 <= next_x < N and 0 <= next_y < N and grid[next_x][next_y] == 1:
                    DFS(next_x, next_y)

        nodes_start = []
        DFS(x, y)


        def BFS():
            step = 0
            q = deque(nodes_start)
            while q:
                cur_l = len(q)
                for _ in range(cur_l):
                    cur_x, cur_y = q.popleft()
                    for d in dir:
                        next_x, next_y = cur_x + d[0], cur_y+d[1]
                        if 0 <= next_x < N and 0 <= next_y < N:
                            if grid[next_x][next_y] == 0:
                                q.append((next_x, next_y))
                                grid[next_x][next_y] = -1
                            elif grid[next_x][next_y] == 1:
                                return step
                step += 1
            return step

        res = BFS()
        return res

print(Solution().shortestBridge(grid = [[0,1],[1,0]]))
print(Solution().shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))
print(Solution().shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))