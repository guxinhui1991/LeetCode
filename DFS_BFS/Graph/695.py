from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        l, r, t, b = 0, w - 1, 0, h - 1
        res = 0
        directions = [(0,1), (-1,0), (0,-1), (1,0)]

        def DFS(x, y):
            nonlocal res, l, r, t, b, count
            if x<t or x>b or y<l or y>r: return False

            res = max(res, count)
            grid[x][y] = 0
            visited[x][y] = True

            for d in directions:
                next_x, next_y = x + d[0], y + d[1]
                if 0<=next_x<h and 0<=next_y<w and grid[next_x][next_y] and not visited[next_x][next_y]:
                    count += 1
                    DFS(next_x, next_y)

        visited = [[False for _ in range(w)] for _ in range(h)]

        for i in range(h):
            for j in range(w):
                if grid[i][j] and not visited[i][j]:
                    count = 1
                    DFS(i, j)

        return res



print(Solution().maxAreaOfIsland([[1,1,1],[1,0,0]]))

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
