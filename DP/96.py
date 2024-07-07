#   Memorization
class Solution1(object):
    def __init__(self):
        self.memo = {}
        self.memo[0] = 1
        self.memo[1] = 1
        self.memo[2] = 2
    def numTrees(self, n):
        if n in self.memo: return self.memo[n]
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        self.memo[n] = res
        return res

#   Tabulation
class Solution2:
    def numTrees(self, n: int) -> int:
        if n <= 2: return n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(2, n+1):
            dp[i] = sum([dp[i-j-1]*dp[j] for j in range(i)])
        return dp[-1]


print(Solution1().numTrees(3))
print(Solution1().numTrees(4))
print(Solution1().numTrees(5))

print(Solution2().numTrees(3))
print(Solution2().numTrees(4))
print(Solution2().numTrees(5))