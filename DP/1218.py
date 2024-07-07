class Solution(object):
    def longestSubsequence(self, arr, d):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """

        if (not arr): return 0

        dp = {}

        for i, val in enumerate(arr):
            if val - d in dp:
                dp[val] = dp[val-d] + 1
            else:
                dp[val] = 1

        return max(dp.values())

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
Solution().longestSubsequence(arr, difference)