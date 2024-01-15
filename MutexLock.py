#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:19:31 2017

@author: Xinhui
"""
#from threading import Thread, Lock
#
#mutex = Lock()
#
#def processData(data):
#    mutex.acquire()
#    try:
#        print('Do some stuff')
#    finally:
#        mutex.release()
#
#while True:
#    haystack = Thread(target = processData, args = (some_data,))
#    haystack.start()
#    

from multiprocessing import Process, Lock

mutex = Lock()

def processData(data):
    with mutex:
        print('Do some stuff')

if __name__ == '__main__':
    while True:
        p = Process(target = processData, args = (some_data,))
        p.start()