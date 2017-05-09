#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 07:46:06 2017

@author: brendontucker
"""

# brute force
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)