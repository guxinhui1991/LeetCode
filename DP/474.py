class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


        for i,s in enumerate(strs):
            num_0 = sum([i=="0" for i in s])
            num_1 = sum([i=="1" for i in s])
            for x in range(n, num_1-1, -1):
                for y in range(m, num_0-1, -1):
                    dp[x][y] = max(dp[x][y], dp[x-num_1][y-num_0]+1)


        return dp[-1][-1]

print(Solution().findMaxForm(strs = ["10","0001","111001","1","0"], m = 3, n = 3))
print(Solution().findMaxForm(strs = ["10","0","1"], m = 1, n = 1))
