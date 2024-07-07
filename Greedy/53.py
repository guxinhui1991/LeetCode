import sys
from typing import List


## Version 2018
class Solution:
    def maxSubarray(self, nums):
        """
       :type nums: List[int]
       :rtype: int
       """

        if (len(nums) <= 1): return max(0, nums[0])

        # Denote students[i] as largest sum until index i
        A = [0] * len(nums)
        tmpSum = nums[0]
        A[0] = nums[0]

        for i in range(1, len(nums)):
            A[i] = max(nums[i], A[i - 1] + nums[i])

            if A[i] > tmpSum: tmpSum = A[i]
        return tmpSum

## Version Apr 2023
class Solution2(object):

    # Greedy
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if(N <=1): return sum(nums)
        cur_sum = 0
        max_sum = -sys.maxsize
        for i in range(N):
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
            cur_sum = max(0, cur_sum)

            ####################################################################################
            #   Kodane's Algorithm
            #   for each i, find cur_sum, max_sum ending at index i
            ####################################################################################
            '''
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
            '''
        return max_sum

    # DP
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        for i in range(1, N):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return max(dp)

if __name__ == '__main__':
    nums = [-2,1]
    print(Solution2().maxSubArray(nums))
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution2().maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print(Solution2().maxSubArray(nums))
    print(Solution().maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubarray([1.0, 2.0, -5.0, 4.0, -3.0, 2.0, 6.0, -5.0, -1.0]))


