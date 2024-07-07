from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        N = len(prices)

        dp = [[0 for _ in range(N + 1)] for _ in range(2 * k )]

        for i, dp_i in enumerate(dp):
            if i % 2 == 0:
                dp_i[0] = -prices[0]

        for i in range(1, N+1):
            dp_0 = dp[0]
            dp_0[i] = max(dp_0[i-1], -prices[i-1])
            dp_prev = dp_0
            for j in range(1, 2*k + 1):
                dp_j = dp[j-1]
                if (j-1) % 2:
                    dp_j[i] = max(dp_j[i - 1], dp_prev[i - 1] + prices[i-1])
                else:
                    dp_j[i] = max(dp_j[i - 1], dp_prev[i - 1] - prices[i-1])

                dp_prev = dp_j
        return dp[-1][-1]

print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
print(Solution().maxProfit(2, [1, 2, 3, 4, 5]))