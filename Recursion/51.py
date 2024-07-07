import copy
from typing import List


def checkValid(res):
    v = [sum(res[i]) for i in range(n)]
    h = [sum(x) for x in zip(*res)]
    expected = [1 for _ in range(n)]
    return v == expected and h == expected


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        board_curr =[['.' for _ in range(n)] for _ in range(n)]
        output = []

        def checkValid(board, row, col):
            nonlocal n
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # 45'
            i_u, j_u = -1, -1
            while 0 <= row + i_u < n and 0 <= col + j_u < n:
                if board[row + i_u][col + j_u] == 'Q':
                    return False
                i_u -= 1
                j_u -= 1
            # 135'
            i_d, j_d = -1, +1
            while 0 <= row + i_d < n and 0 <= col + j_d < n:
                if board[row + i_d][col + j_d] == 'Q':
                    return False
                i_d -= 1
                j_d += 1

            return True

        def dfs(r):
            nonlocal n
            if r == n :

                #output.append(copy.deepcopy(board_curr))
                output.append(["".join(i) for i in board_curr])
                return

            for col in range(n):
                if checkValid(board_curr, r, col):
                    board_curr[r][col] = 'Q'
                    dfs(r+1)
                    board_curr[r][col] = '.'

        dfs(0)
        return output


print(Solution().solveNQueens(4))