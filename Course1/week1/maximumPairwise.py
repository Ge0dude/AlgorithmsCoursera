#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 07:46:06 2017

@author: brendontucker
"""

#
##input info
#n = int(input())
#a = [int(x) for x in input().split()]
#assert(len(a) == n)


#brute force
#
#for i in range(0, n):
#    for j in range(i+1, n):
#        if a[i]*a[j] > result:
#            result = a[i]*a[j]
#
#print(result)

n = 3
a = [1, 2, 3]
result = 0


first = 0
second = 0
for x in range(0, n):
    if a[x] > first:
        second = first
        first = a[x]
    elif a[x] > second:
        second = a[x]
        
result = first * second
print(result)