from typing import List


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        N = len(stones)
        nums_target = sum(stones) // 2

        dp = [0 for _ in range(15000)]

        for i, num in enumerate(stones):
            for j in range(nums_target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return sum(stones) - 2 * dp[nums_target]

    #Dec 2023
    def lastStoneWeightII_2(self, stones: List[int]) -> int:

        target = sum(stones)//2
        dp = [[0 for _ in range(target+1)] for _ in range(len(stones)+1)]

        for i in range(1, len(stones)+1):
            for j in range(1, target+1):
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i-1]]+stones[i-1])



        return sum(stones) - dp[-1][-1] - dp[-1][-1]

print(Solution().lastStoneWeightII([8,2,4,4,8]))
print(Solution().lastStoneWeightII_2([8,2,4,4,8]))
print(Solution().lastStoneWeightII([2,7,4,1,8,1]))
print(Solution().lastStoneWeightII_2([2,7,4,1,8,1]))
print(Solution().lastStoneWeightII([31,26,33,21,40]))
print(Solution().lastStoneWeightII_2([31,26,33,21,40]))
