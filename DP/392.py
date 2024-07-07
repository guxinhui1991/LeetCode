class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        dp = [[0 for _ in range(len_t+1)] for _ in range(len_s+1)]

        for j in range(1, len_s+1):
            for i in range(1, len_t+1):
                if t[i-1] == s[j-1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = dp[j][i - 1]

        return dp[-1][-1] == len_s

    def isSubsequence2(self, s: str, t: str) -> bool:
        if not s : return True
        if len(s) > len(t): return False
        for i in range(len(t)):
            if t[i] == s[0]:
                return self.isSubsequence2(s[1:], t[i+1:])

        return False

print(Solution().isSubsequence1("abc", "ahbgdc"))
print(Solution().isSubsequence2("abc", "ahbgdc"))
print(Solution().isSubsequence1("bb", "ahbgdc"))
print(Solution().isSubsequence2("bb", "ahbgdc"))