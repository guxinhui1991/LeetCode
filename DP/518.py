from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # dp[i] : Number of Combinations make up to amount i
        dp = [0 for _ in range(amount + 1)]
        coins = [c for c in coins if c<=amount]
        dp[0] = 1
        for i, c in enumerate(coins):
            dp[c] += 1
            for j in range(c+1, amount+1):
                #dp[j] = max(dp[j], dp[j-c], dp[c])
                dp[j] = dp[j]+ dp[j-c]

        return dp[amount]


print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 5, coins = [1,2,5]))