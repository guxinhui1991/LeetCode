#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:59:51 2017

@author: Xinhui
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        n_start = newInterval.start
        n_end = newInterval.end
        