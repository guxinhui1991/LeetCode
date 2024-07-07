from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        nums = [c for c in nums if c<=target]
        dp[0] = 1
        for j in range(target+1):
            for i, c in enumerate(nums):
                if j >= c:
                    dp[j] = dp[j]+ dp[j-c]
                #dp[j] = dp[j]*dp[j-c]

        return dp[target]


print(Solution().combinationSum4(nums = [1,2,3], target = 4))