class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(k + 1)]
        for x in range(m):
            dp[0][x][0] = 0
            dp[1][x][1] = 1

        for x in range(n):
            for y in range(m):
                for z in range(k):
                    dp[x][y][z] = dp[x - 1][y][z] * x


        return dp[n][m][k]

print(Solution().numOfArrays(2, 3, 1), end="")
