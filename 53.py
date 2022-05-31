#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:16:56 2021

@author: xinhui
"""


class Solution:
    def maxSubarray(self, nums):
        """
       :type nums: List[int]
       :rtype: int
       """

        if (len(nums) <= 1): return max(0, nums[0])

        # Denote A[i] as largest sum until index i
        A = [0] * len(nums)
        tmpSum = nums[0]
        A[0] = nums[0]

        for i in range(1, len(nums)):
            A[i] = max(nums[i], A[i - 1] + nums[i])

            if A[i] > tmpSum: tmpSum = A[i]
        return tmpSum


if __name__ == '__main__':
    print(Solution().maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubarray([1.0,2.0, -5.0, 4.0, -3.0, 2.0, 6.0, -5.0, -1.0]))
