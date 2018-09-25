#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:57:02 2017

@author: Xinhui
"""
import time

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if(length == 0):
            return 0
        substr = []
        start, end = 0, 0
        for i in range(length):
            curr = s[start:end]
            while(i<length and s[i] not in curr):
                curr = curr +s[i]
                i = i+1
            start=i
            end = i
            substr.append(curr)
        return len(max(substr, key=len))

#class Solution:
#    # @return an integer
#    def lengthOfLongestSubstring(self, s):
#        start = maxLength = 0
#        usedChar = {}
#        
#        for i in range(len(s)):
#            if s[i] in usedChar and start <= usedChar[s[i]]:
#                start = usedChar[s[i]] + 1
#            else:
#                maxLength = max(maxLength, i - start + 1)
#
#            usedChar[s[i]] = i
#
#        return maxLength
#    


#start = time.time()
print(Solution().lengthOfLongestSubstring('dvdfsdfadfgergrtgascasdfdgearferasdc'))
#end = time.time()
#print end - start