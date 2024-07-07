from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        res = 0
        h, w = len(grid), len(grid[0])

        ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = [[False for _ in range(w)] for _ in range(h)]


        def DFS(x, y):
            nonlocal res, h, w
            visited[x][y] = True
            grid[x][y] = 0
            for d in ds:
                next_x, next_y = x + d[0], y + d[1]
                if 0<next_x<h and 0<next_y<w and not visited[next_x][next_y] and grid[next_x][next_y]:
                    res += 1
                    DFS(next_x, next_y)

        for i in range(h):
            visited[i][0] = True
            visited[i][-1] = True
            if grid[i][0]: DFS(i, 0)
            if grid[i][w-1]: DFS(i, w-1)
        for i in range(w):
            visited[0][i] = True
            visited[-1][i] = True
            if grid[0][i]: DFS(0, i)
            if grid[h-1][i]: DFS(h-1, i)


        res = 0
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                if grid[i][j] and not visited[i][j]:
                    res += 1
                    DFS(i, j)

        return res

print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(Solution().numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))