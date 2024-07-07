from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N, M = len(board), len(board[0])

        def backTracking(t, x, y):

            if t == "": return True
            if x<0 or y<0 or x >= N or y >= M: return False

            if board[x][y] == t[0]:
                board[x][y] = "0"
                if backTracking(t[1:], x-1, y): return True
                if backTracking(t[1:], x+1, y): return True
                if backTracking(t[1:], x, y+1): return True
                if backTracking(t[1:], x, y-1): return True
                board[x][y] = t[0]

            return False

        for i in range(N):
            for j in range(M):
                if backTracking(word, i, j):
                    return True


        return False


print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))






