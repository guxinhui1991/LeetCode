#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 07:57:02 2017

Problem:
Length of the longest substring without repeating characters
Given a string str, find the length of the longest substring without repeating characters.

For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
For “BBBB” the longest substring is “B”, with length 1.
For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7

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
        return len(max(substr, key=len)), max(substr, key=len)

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
print(Solution().lengthOfLongestSubstring('ABDEFGABEF'))
print(Solution().lengthOfLongestSubstring('AAAAAA'))
#end = time.time()
#print end - start