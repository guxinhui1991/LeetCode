import sys
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        N, M = len(grid), len(grid[0])

        num_b = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    num_b += 1


        def bfs(x, y, visited):
            q = deque([])
            q.append((x, y))
            visited[x][y] = True
            cur_step, total_step = 0, 0
            cur_b = 0
            while q:

                cur_len = len(q)
                cur_step += 1
                for _ in range(cur_len):
                    cur_x, cur_y = q.popleft()

                    for i in range(4):
                        next_x = cur_x + dir[i][0]
                        next_y = cur_y + dir[i][1]
                        if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                            continue

                        if grid[next_x][next_y] == 2:
                            visited[next_x][next_y] = True
                            continue

                        if not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            if grid[next_x][next_y] == 1:
                                cur_b += 1
                                total_step += cur_step
                                if cur_b == num_b: return total_step
                                continue
                            q.append((next_x, next_y))
            if cur_b != num_b:
                for row in range(N):
                    for col in range(M):
                        if grid[row][col] == 0 and visited[row][col]:
                            grid[row][col] = 2
                return float('inf')
            return total_step

        dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        res = sys.maxsize
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    visited = [[False for _ in range(M)] for _ in range(N)]
                    res = min(bfs(i, j, visited), res)
        return -1 if res == sys.maxsize else res