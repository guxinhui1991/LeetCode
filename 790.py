class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        # if(N<=0): return 0
        # elif(N==1): return 1
        # elif(N==2): return 2
        # elif(N==3): return 5

        dp = [[0, 0] for i in range(N+1)]
        dp[0][0], dp[1][0] = 1, 1
        K = 10**9 + 7

        for i in range(2, N+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2 *dp[i-1][1])%K
            dp[i][1] = (dp[i-1][1] + dp[i-2][0])%K
        return dp[N][0]


print(Solution().numTilings(3))
print(Solution().numTilings(4))
print(Solution().numTilings(5))