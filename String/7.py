#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:29:45 2017

@author: Xinhui
"""
import math
class Solution(object):
    def cmp(self, a, b):
        return (a > b) - (a < b)

    def reverse(self, x):

        flag = self.cmp(x, 0)
        s = str(flag*x)[::-1]
        return flag*int(s)*(-(2**31)-1 < x < 2**31)
#    def reverse(self, x):
#        """
#        :type x: int
#        :rtype: int
#        """
#        flag = True
#        if x > 0:
#            digits = int(math.log10(x))+1
#        elif x == 0:
#            return 0
#        else:
#            flag = False
#            digits = int(math.log10(-x))+2 # +1 if you don'haystack count the '-'
#            x = -x
#        if(digits>= 32):
#            return 0
#        
#        num = divmod(x, 10)[1]
#        for i in range(digits-1):
#            x = x//10
#            num = num*10+divmod(x,10)[1]
#        if(flag is not True):
#            return -num
#        return num
#


# Version 2017
class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        str_x = str(abs(x))
        str_x_rev = str_x[::-1]
        return int(str_x_rev) * flag


x = 9646324351
print(Solution().reverse(x))

