
# DP method
# Jan 2024

class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        cur_max = 0
        l, r = 0, 0
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if j - i + 1 > cur_max and dp[i][j]:
                    l, r = i, j
                    cur_max = r - l + 1

        return s[l:r + 1]

#
#   Two pointer
#   Feb 2021
#
class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        if(len(s) <= 1): return s;

        start, end = 0, 0
        for i in range(len(s)):
            res1 = self.expandFromMiddle(s, i, i)
            res2 = self.expandFromMiddle(s, i, i + 1)

            tempRes = max(res1, res2)
            if(tempRes > (end - start + 1)):
                start = i - int((tempRes-1)/2)
                end = i + int(tempRes/2)
            res = s[start:end+1]
        return res
    def expandFromMiddle(self, s, start, end):
        if (start > end): return 0

        while ((start >= 0) and (end < len(s)) and (s[start] == s[end])):
            start = start - 1
            end = end + 1

        return end - start - 1