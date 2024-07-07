import copy
from collections import deque
from typing import List


class Solution_DFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        l, r, t, b = 0, w-1, 0, h-1
        res = 0

        def DFS(x, y):
            nonlocal grid
            nonlocal l, r, t, b
            if x<t or x>b or y<l or y>r: return

            grid[x][y] = "0"
            if x-1 >=0 and grid[x-1][y] == "1": DFS(x-1, y)
            if x+1 < h and grid[x+1][y] == "1": DFS(x+1, y)
            if y-1 >=0 and grid[x][y-1] == "1": DFS(x, y-1)
            if y+1 < w and grid[x][y+1] == "1": DFS(x, y+1)
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1":
                    res += 1
                    DFS(i, j)

        return res


class Solution_BFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        l, r, t, b = 0, w-1, 0, h-1
        ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = [[False for _ in range(w)] for _ in range(h)]

        def BFS(x, y):
            q = deque([(x, y)])
            visited[x][y] = True

            while q:
                cur_x, cur_y = q.popleft()
                for d in ds:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    # Important -- NOT return in DFS case.
                    if next_x < t or next_x > b or next_y < l or next_y > r:
                        continue
                    if not visited[next_x][next_y] and grid[next_x][next_y] == "1":
                        q.append((next_x, next_y))
                        visited[next_x][next_y] = True

        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    BFS(i, j)

        return res


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution_DFS().numIslands(copy.deepcopy(grid)))
print(Solution_BFS().numIslands(copy.deepcopy(grid)))