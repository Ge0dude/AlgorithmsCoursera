#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:57:20 2017

@author: brendontucker

mainly an exploration file to understand problem growth not to implement an 
efficient solution
modVar-- 2, 3, 4, 5, 6
length-- 4, 8, 5, 20, 24 
"""

#n = int(input())
n = 50
m = 5
resultList = [0, 1]
modVarList = [0, 1]
result = 0
zeroBool = False
oneBool = False
#twoBool = False
if n == 0:
    result = 0
elif n == 1:
    result = 1
else:
    n += 1
    for x in range(2, n):
        newNum = resultList[x-2] + resultList[x-1]
        resultList.append(newNum)
        modNum = newNum % m
        if x > 3:
            if modVarList[-1] == 1:
               if modVarList[-2] == 1:
                   if modVarList[-3] == 0:
                       break
        
        modVarList.append(modNum)

        
        
        
        
        
        
        
        
        
        
        
'''
if modNum == 0:
            if zeroBool == True:
                zeroBool = False
            else:
                zeroBool = True
        elif modNum == 1:
            if zeroBool == True:
                if oneBool == True:
                    break#exit logic here we have the period
            else:
                oneBool = True
            else:
                zeroBool = False
        
        #here is where I could check for 011 sequence
'''        
