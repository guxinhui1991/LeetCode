from typing import List


class Solution(object):

    # Apr 2023
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        totalSum = 0

        for i, val in enumerate(prices[1:]):
            curDiff = prices[i + 1] - prices[i]
            if curDiff > 0:
                totalSum += curDiff
        return totalSum

    def maxProfit2(self, prices: List[int]) -> int:

        cur_profit = 0
        prev_low = [0 for _ in range(len(prices))]

        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                prev_low[i] = i-1
            else:
                prev_low[i] = i

        for i in range(len(prices)):
            if prev_low[i] != i:
                cur_profit += prices[i] - prices[prev_low[i]]

        return cur_profit


    # Dynamic Programming
    def maxProfit_DP(self, prices: List[int]) -> int:

        # dp[i][0] -> max profit if holding stock on day i
        # dp[i][1] -> max profit if not holding stock on day i
        dp = [[0 for _ in range(2)]for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            print (i, " : ", dp[i][0], " : ", dp[i][1])



        return dp[-1][-1]



prices =[7,1,5,3,6,4]
#print(Solution().maxProfit(prices))
#print(Solution().maxProfit2(prices))
print(Solution().maxProfit_DP(prices))