#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 07:46:15 2017

@author: brendontucker

maybe I need to abandon arrays--might be taking too long, saw someone who
claimed that they only used three variables. This might be more efficient
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
        newNum = (resultList[x-2] + resultList[x-1])%10
        resultList.append(newNum)
    result = resultList[-1]
    
print(result)















'''
n = int(input())
#n = 999999
if n == 0:
    result = 0
elif n == 1:
    result = 1
else:
    counter = 2
    small = 0
    big = 1
    while counter <= n:
        curr = small + big
        small = big
        big = curr
        counter += 1
        
    
#result = str(curr) 
print(curr%10)
'''












