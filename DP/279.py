class Solution:
    def numSquares(self, n: int) -> int:
        if n <=1: return 1

        candidates = []
        for i in range(1, 101):
            if i**2 <= n:
                candidates.append(i**2)
            else:
                break
        CUR_MAX = 101**2

        dp = [CUR_MAX for _ in range(n+1)]
        dp[0] = 0
        for j in range(n + 1):
            for i,val in enumerate(candidates):
                if j >= val:
                    dp[j] = min(dp[j], dp[j-val]+1)
        return dp[n]


print(Solution().numSquares(4))
print(Solution().numSquares(1))
print(Solution().numSquares(2))
print(Solution().numSquares(12))
print(Solution().numSquares(13))