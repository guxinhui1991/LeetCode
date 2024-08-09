from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def DFS(x, y):
            nonlocal N, M, idx, count
            count += 1
            vis[x][y] = idx
            for d in dir:
                next_x, next_y = x + d[0], y +d[1]
                if 0 <= next_x < N and 0 <= next_y < M and grid[next_x][next_y] and vis[next_x][next_y] == 0:
                    DFS(next_x, next_y)


        N, M = len(grid), len(grid[0])
        vis = [[0 for _ in range(M)] for _ in range(N)]
        island_size = {}
        idx = 1
        for i in range(N):
            for j in range(M):
                if grid[i][j] and vis[i][j] == 0:
                    count = 0
                    DFS(i, j)
                    island_size[idx] = count
                    idx += 1

        if (island_size and max(island_size.values()) == N * M): return N * M
        res = 1
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0 and vis[i][j] == 0:
                    adj = set()
                    for d in dir:
                        x, y = i + d[0], j + d[1]
                        if 0 <= x < N and 0 <= y < M and vis[x][y]:
                            adj.add(vis[x][y])
                    if adj: res = max(res, 1+sum([island_size[i] for i in adj]))

        return res

print(Solution().largestIsland([[1,0],[0,1]]))
print(Solution().largestIsland([[1,1],[1,1]]))
print(Solution().largestIsland([[1,1],[1,0]]))
print(Solution().largestIsland([[1,1,1],[1,1,1],[1,1,1]]))