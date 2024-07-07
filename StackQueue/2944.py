from collections import deque
from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:

        N = len(prices)
        dp = [0 for _ in range(N + 1)]

        def helper(start):
            nonlocal prices, dp, N
            if start >= N: return 0
            if dp[start]: return dp[start]

            res = float('inf')

            for i in range(start + 1, (start + 1) * 2 + 1):
                res = min(res, helper(i))
            dp[start] = res + prices[start]

            return dp[start]

        return helper(0)

    def minimumCoins2(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        q = deque()
        for i in range(n):
            while q and (q[0] + 1) * 2 < i + 1:
                q.popleft()
            while q and dp[q[-1]] + A[q[-1]] >= dp[i] + A[i]:
                q.pop()
            q.append(i)
            dp[i + 1] = dp[q[0]] + A[q[0]]
        return dp[-1]
print(Solution().minimumCoins([3,1,2]))
Solution().minimumCoins([26,18,6,12,49,7,45,45])
Solution().minimumCoins2([26,18,6,12,49,7,45,45])