from collections import deque
from typing import List


class Solution_DFS:
    def allPathsSourceTarget(self, d: List[List[int]]) -> List[List[int]]:

        def DFS(n, cur):
            nonlocal res, N
            if n == N - 1:
                res.append(cur)
                return
            for j in d[n]:
                DFS(j, cur + [j])

        N = len(d)
        res = []
        for i in d[0]:
            DFS(i, [0] + [i])

        return res

print(Solution_DFS().allPathsSourceTarget([[1,2],[3],[3],[]]))