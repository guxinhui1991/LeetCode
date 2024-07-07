import sys
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        N, M = len(image), len(image[0])
        U, D, L, R = 0, N-1, 0, M-1
        u, d, l, r = N-1, 0, M-1,0


        def DFS(x, y):
            nonlocal image
            nonlocal u, d, l, r
            if x < U or x > D or y < L or y > R: return
            if image[x][y] == '1':
                u = min(x, u)
                d = max(x, d)
                l = min(y, l)
                r = max(y, r)

                image[x][y] = 0
                DFS(x+1, y)
                DFS(x-1, y)
                DFS(x, y+1)
                DFS(x, y-1)
            else:
                return

        DFS(x, y)
        return (r-l+1) * (d-u+1)

print(Solution().minArea(image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2))

print(Solution().minArea(image = [["1","1"]], x = 0, y = 1))