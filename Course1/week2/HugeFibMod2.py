#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:30:54 2017

@author: brendontucker
"""

import sys

input = sys.stdin.read();
n, m = map(int, input.split())
n, m = map(int, input.split())
#n = 2816213588
#m = 30524
resultList = [0, 1]
modVarList = [0, 1]
small = 0
big = 1

n += 1
for x in range(2, n):
    curr = small + big
    resultList.append(curr)
    resultList.pop(0)
    small = big
    big = curr
    modNum = curr % m
    if x > 3:
        if modVarList[-1] == 1:
           if modVarList[-2] == 1:
               if modVarList[-3] == 0:
                   for x in range(3):
                       modVarList.pop()
                   break
    
    modVarList.append(modNum)

n -= 1 
if n >= m:    
    periodLength = len(modVarList)    
    remainder = n % periodLength
    result = modVarList[remainder]
if m > n:
    result = modVarList[-1]

print(result)





'''
n += 1
    for x in range(2, n):
        newNum = resultList[x-2] + resultList[x-1]
        resultList.append(newNum)
        modNum = newNum % m
        if x > 3:
            if modVarList[-1] == 1:
               if modVarList[-2] == 1:
                   if modVarList[-3] == 0:
                       for x in range(3):
                           modVarList.pop()
                       break
        
        modVarList.append(modNum)
'''