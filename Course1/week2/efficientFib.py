#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:57:34 2017

@author: brendontucker
"""
n = int(input())
#n = 2
resultList = [0, 1]
result = 0
if n == 0:
    result = 0
elif n == 1:
    result = 1
else:
    n += 1
    for x in range(2, n):
        newNum = resultList[x-2] + resultList[x-1]
        resultList.append(newNum)
    result = resultList[-1]
    
print(result)


