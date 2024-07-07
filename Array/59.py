class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        n_steps = n ** 2
        res = [[0] * n for _ in range(n)]

        i, j, di, dj = 0, 0, 0, 1
        for step in range(n_steps):
            res[i][j] = step + 1
            if res[(i+di)%n][(j+dj)%n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return res

print(Solution().generateMatrix(4))
print(Solution().generateMatrix(6))