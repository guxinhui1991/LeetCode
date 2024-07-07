from typing import List


class Solution(object):
    def canPartition(self, nums):
        if (sum(nums) % 2): return False

        N = len(nums)
        nums_target = sum(nums) // 2

        dp = [0 for _ in range(10000)]

        for i, num in enumerate(nums):
            for j in range(nums_target, num-1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[nums_target] == nums_target


class Solution_dp2(object):
    def canPartition_dp2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        N = len(nums)
        maxM = 10000
        if (sum(nums) % 2): return False

        nums_target = sum(nums) // 2
        nums.sort()

        dp = [[0 for _ in range(maxM+1)] for _ in range(N)]

        for i in range(N):
            for j in range(maxM, -1, -1):
                dp[i][j] = min(j, max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i]))

        # print(dp)
        return dp[-1][nums_target]==nums_target

    # Dec 2023
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2: return False

        target = sum(nums) // 2
        dp = [[0 for _ in range(target)] for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            for j in range(target):
                dp[i][j] = dp[i-1][j]
                if nums[i-1] == j+1: dp[i][j] = j+1
                if nums[i-1] < j+1: dp[i][j] = min(j+1, max(dp[i - 1][j - nums[i-1]] + nums[i-1], dp[i - 1][j]))

        return dp[-1][-1] == target


print(Solution().canPartition(nums=[1,5,11,5]))
print(Solution_dp2().canPartition(nums=[1,5,11,5]))
print(Solution_dp2().canPartition_dp2(nums=[1,5,11,5]))