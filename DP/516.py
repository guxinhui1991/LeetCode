class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        dp[i][j]: the longest palindromic subsequence in needle[i:j+1]

        """

        dp = [[0] * len(s) for _ in range(len(s))]
        dp[0][0] = 1

        for i in reversed(range(len(s))):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])


        return dp[0][-1]

    # Recursive method with memorization
    def longestPalindromeSubseq2(self, s: str) -> int:
        memo = {}

        def helper(i, j):
            if i > j: return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == s[j]:
                memo[(i, j)] = helper(i + 1, j - 1) + 2
            else:
                memo[(i, j)] = max(helper(i + 1, j), helper(i, j - 1))

            return memo[(i, j)]

        N = len(s)
        for i in range(N):
            memo[(i, i)] = 1

        return helper(0, N - 1)


print(Solution().longestPalindromeSubseq("bbbab"))
print(Solution().longestPalindromeSubseq2("bbbab"))
# print(Solution().longestPalindromeSubseq("cbbd"))
