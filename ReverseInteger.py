#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:29:45 2017

@author: Xinhui
"""
import math
class Solution(object):
    
    def reverse(self, x):
#        s = cmp(x, 0)
#        r = int(`s*x`[::-1])
#        return s*r * (r < 2**31)

        flag = cmp(x, 0)
        s = str(flag*x)[::-1]
        return flag*int(s)*(x<pow(2, 32))
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
#            digits = int(math.log10(-x))+2 # +1 if you don't count the '-' 
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
print(Solution().reverse(0))

