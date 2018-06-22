#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 17:50:00 2017

@author: Xinhui
"""
#
#class Solution(object):
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
#        l=len(nums)
#        pos1, pos2 = 0, 0
#        sol = [pos1, pos2]
#        for i in range(l):
#            for j in range(i+1, l):
#                if(target-nums[i] == nums[j]):
#                    sol[0] = i
#                    sol[1] = j
#                    return sol
#        return sol



## Solution
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

testin = [3,2,4]
target = 6
print(Solution().twoSum(testin, target))

