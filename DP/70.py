class Solution:

    # DP solution
    def climbStairs(self, n: int) -> int:

        dp = [0 for _ in range(n+1)]
        steps = [1,2]
        dp[0] = 1
        for i in range(n+1):
            for k, step in enumerate(steps):
                if i >= step: dp[i] = dp[i-step] + dp[i]


        return dp[n]

print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))