#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 07:46:06 2017

@author: brendontucker
"""


'''#input info
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
'''
n = 11
a = [10, 12, 3, 4, 5, 1, 1, 3, 12, 15, 4]
result = 0

#brute force
#
#for i in range(0, n):
#    for j in range(i+1, n):
#        if a[i]*a[j] > result:
#            result = a[i]*a[j]
#
#print(result)

first = 0
second = 0
for x in range(0, n):
    if x > first:
        first = x
    elif x > second:
        second = x
        
result = first * second
print(result)