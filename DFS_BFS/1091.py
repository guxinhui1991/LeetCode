import copy
from collections import deque
from typing import List
import timeit


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dirs = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        vis =[[0 for _ in range(N)] for _ in range(N)]
        if grid[0][0] or grid[-1][-1] != 0: return -1
        q = deque([(0, 0)])
        vis[0][0] = 1
        step = 1
        while q :
            cur_len = len(q)
            for _ in range(cur_len):
                x, y = q.popleft()
                if x == y == N - 1: return step
                for d in dirs:
                    n_x, n_y = x + d[0], y + d[1]
                    if 0<=n_x<N and 0<=n_y<N and vis[n_x][n_y]==0 and grid[n_x][n_y]==0:
                        q.append((n_x, n_y))
                        vis[n_x][n_y] = step

            step += 1
        return -1


print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))
print(Solution().shortestPathBinaryMatrix([[0,1],[1,0]]))
