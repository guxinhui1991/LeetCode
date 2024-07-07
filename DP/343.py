class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0], dp[1] = 0, 1

        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], (i-j) * j , (i-j) * dp[j])

        return dp[-1]

class Solution2:
    def __init__(self):
        self.d = {2: 1}

    def integerBreak(self, n: int) -> int:
        if n in self.d: return self.d[n]
        res = -float('inf')
        for i in range(2, n):
            if i in self.d:
                res = max(res, self.d[i])
            else:
                c = (n + 1 - i) * self.integerBreak(i)
                self.d[i] = c
                res = max(res, c)
        return res


Solution2().integerBreak(3)