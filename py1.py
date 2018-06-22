#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:32:03 2017

@author: Xinhui
"""

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue= alist[index]
        position = index
        
        while position>0 and alist[position-1]>currentValue:
            alist[position]=alist[position-1]
            position = position-1
        
        alist[position]=currentValue

alist = [54,26,93,17,77,31,44,55,20]
print(insertionSort(alist))


def bubbleSort(alist):
    for index in range(0,len(alist)):
        position = 0
        while position<(len(alist)-index-1):
            if (alist[position]>alist[position+1]):
                alist[position], alist[position+1] = alist[position+1], alist[position]
            position = position+1
    return alist

print(bubbleSort([3,4,1,2]))



def selectionSort(alist):
    for i in range(len(alist)):
        alist[range(len(alist)-i)] = getMax(alist[range(len(alist)-i)])
    return alist

def getMax(alist):
    position = 0
    for i in range(len(alist)):
        if(alist[i]>maxNum):
            index = i
    alist[i], alist[len(alist)-1] = alist[len(alist)-1],alist[i]
    return alist

print(bubbleSort([54,26,93,17,77,31,44,55,20]))


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    
    return alist
print(mergeSort([54,26,93,17,77,31,44,55,20]))


def quickSort(alist, first = 0, last = len(alist)-1):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
