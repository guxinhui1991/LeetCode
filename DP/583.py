class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1, N2 = len(word1), len(word2)
        dp = [[0 for _ in range(N1 + 1)] for _ in range(N2+1)]

        for i in range(1, N2+1):
            for j in range(1, N1+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j]=dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return N1 + N2 - 2*dp[-1][-1]


Solution().minDistance("sea", "eat")