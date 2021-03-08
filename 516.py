class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        dp[i][j]: the longest palindromic subsequence's length of substring(i, j)
        here i, j represent left, right indexes in the string
        """

        dp = [[0] * len(s) for _ in range(len(s))]
        dp[0][0] = 1

        for i in reversed(range(len(s) - 1)):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])


        return dp[0][-1]


print(Solution().longestPalindromeSubseq("bbbab"))
# print(Solution().longestPalindromeSubseq("cbbd"))
