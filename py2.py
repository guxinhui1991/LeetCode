#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:44:49 2017

@author: Xinhui
"""

class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
            
            
x = Restaurant()
print(x.bankrupt)
print(Restaurant().bankrupt)