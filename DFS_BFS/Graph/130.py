from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        N, M = len(board), len(board[0])
        ds = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        visited = [[False for _ in range(M)] for _ in range(N)]

        def DFS(x, y, override=False):

            visited[x][y] = True
            if override: board[x][y] = "X"
            q = deque([(x, y)])
            while q:
                cur_x, cur_y = q.popleft()
                for d in ds:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y] and board[next_x][
                        next_y] == "O":
                        DFS(next_x, next_y, override)

        for i in range(N):
            visited[i][0] = True
            visited[i][M - 1] = True
            if board[i][0] == "O": DFS(i, 0)
            if board[i][M - 1] == "O": DFS(i, M - 1)
        for i in range(M):
            visited[0][i] = True
            visited[N - 1][i] = True
            if board[0][i] == "O": DFS(0, i)
            if board[N - 1][i] == "O": DFS(N - 1, i)

        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if board[i][j] == "O" and not visited[i][j]:
                    DFS(i, j, True)

        return board

Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])