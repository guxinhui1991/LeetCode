from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        N, M = len(mat), len(mat[0])
        res = []
        for i in range(N + M - 1):
            x, y = min(i, N - 1), max(0, i - N + 1)
            val = []
            while x >= 0 and y < M:
               val.append(mat[x][y])
               x -= 1
               y += 1

            if i % 2 == 0: res += val
            else: res += val[::-1]

        return res





        return res

print(Solution().findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]]))