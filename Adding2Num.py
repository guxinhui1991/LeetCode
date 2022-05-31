#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 18:06:25 2017

@author: Xinhui
"""

# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
        
    def print_list(self):
        while self.get_next():
            print(self.get_data())
            self = self.get_next()

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = Node(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = Node(val)
            n = n.next
        return root.next

node1 = Node(2)
node2 = Node(4)
node3 = Node(3)
node1.next = node2
node2.next = node3

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)
node4.next = node5
node5.next = node6

sol = Solution()
print(sol.addTwoNumbers(node1, node4).print_list())