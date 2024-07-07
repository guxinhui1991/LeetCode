class Solution:
    def countSubstrings(self, s: str) -> int:

        def checkPalindrome(s):
            return s==s[::-1]

        N = len(s)

        dp = [0 for _ in range(N + 1)]

        for i in range(1, N + 1):
            count = 0
            for j in range(i):
                if checkPalindrome(s[j:i]):
                    count += 1
            dp[i] = dp[i-1] + count


        return dp[-1]

print(Solution().countSubstrings("aaa"))
print(Solution().countSubstrings("abc"))