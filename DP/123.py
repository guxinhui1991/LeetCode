from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] -> max profit if holding stock on day i
        # dp[i][1] -> max profit if not holding stock on day i
        dp = [[0 for _ in range(4)]for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = -prices[0]
        dp[0][3] = 0


        for i in range(1, len(prices)):

            dp[i][0] = max(dp[i - 1][0], - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])

        print(dp)
        return dp[-1][-1]

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
print(Solution().maxProfit([1,2,3,4,5]))