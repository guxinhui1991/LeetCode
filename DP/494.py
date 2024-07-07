from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums or  (target + sum(nums))%2: return 0
        if abs(target) > sum(abs(i) for i in nums): return 0
        target_l = (target + sum(nums))//2

        dp = [[0 for _ in range(target_l+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for j in range(target_l+1):
                val = nums[i]
                if j>=val:
                    dp[i+1][j] = dp[i][j-val] + dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j]

        return dp[-1][-1]

print(Solution().findTargetSumWays([100], -200))
print(Solution().findTargetSumWays([1], 1))