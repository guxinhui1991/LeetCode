class Solution:

    # Dec 2023
    # DFS_BFS, without memorization
    # TLE
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(str_s, str_t):
            nonlocal memo
            if not str_t: return 1
            if (len(str_s) <= len(str_t)): memo[(str_s, str_t)] = int(str_s==str_t)

            if (str_s, str_t) in memo: return memo[(str_s, str_t)]

            l = dfs(str_s[1:], str_t)

            r = dfs(str_s[1:], str_t[1:]) if str_s[0] == str_t[0] else 0
            memo[(str_s, str_t)] = l+r
            return l+r
        dfs(s, t)
        return memo[(s, t)]



    # DFS_BFS, with memorization
    def numDistinct_DFS(self, s: str, t: str) -> int:
        res = 0
        curr = []
        len_t = len(t)
        def dfs(str_s, str_t):
            nonlocal res, curr, len_t
            if not str_s and str_t: return False

            if len(curr) == len_t and not str_t:
                res+=1
                return

            for i in range(len(str_s)):
                if str_s[i] == str_t[0]:
                    curr.append(str_s[i])
                    dfs(str_s[i+1:], str_t[1:])
                    curr.pop()
            return


        dfs(s, t)

        return res



    # DP- 2d array
    def numDistinct_DP(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]

        for i in range(len_s+1):
            dp[i][0] = 1


        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if t[j-1] == s[i-1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]

print(Solution().numDistinct_DP(s = "rabbbit", t = "rabbit"))
print(Solution().numDistinct_DP(s = "babgbag", t = "bag"))
print(Solution().numDistinct(s = "rabbbit", t = "rabbit"))
print(Solution().numDistinct_DFS(s = "rabbbit", t = "rabbit"))