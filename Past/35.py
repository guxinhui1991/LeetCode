#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 21:00:56 2018

@author: xinhui
"""


#class Solution:
#    def searchInsert(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: int
#        """
#        try:
#            return nums.index(target)
#        except:
#            if(target==nums[-1]):
#                return len(nums)
#            else:
#                for i in range(1,len(nums)):
#                    if (nums[i-1] <= target <= nums[i]):
#                        return i
#                    
#Solution().searchInsert([1,2,3,4], 4)


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    try:
        return nums.index(target)
    except:
        if(target==nums[-1]):
            return len(nums)
        else:
            for i in range(1,len(nums)):
                if (nums[i-1] <= target <= nums[i]):
                    return i


if __name__ == "__main":
    print('Yes')
    res = searchInsert([1,2,3,4], 4)
    print(res)