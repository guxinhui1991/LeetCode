from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        N = 9
        dict_row = [{} for _ in range(N)]
        dict_col = [{} for _ in range(N)]
        dict_box = [{} for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    num = ord(board[i][j]) - ord("0")
                    k = i//3*3 + j//3
                    if num in dict_row[i] or num in dict_col[j] or num in dict_box[k]: return False
                    dict_row[i][num] = dict_col[j][num] = dict_box[k][num] =1


        return True

Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])