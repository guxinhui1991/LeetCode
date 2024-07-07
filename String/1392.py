#################################################################################
#
#   Longest prefix string
#
#################################################################################
class Solution:
    def longestPrefix(self, s: str) -> str:
        N = len(s)
        dp = [0] * N

        for i in range(1, N):
            j = dp[i - 1]

            while j >= 1 and s[j] != s[i]:
                j = dp[j - 1]

            dp[i] = j + (s[j] == s[i])

        return s[:dp[-1]]

