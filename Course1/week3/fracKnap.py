#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 07:59:21 2017

@author: brendontucker

all values and weights are greater than zero--don't have to worry about that
issue

output needs to be maximum value produced from all the fractions
#need to consider teh case where all objects are taken but there is still
    room in the knapsack
"""

n = 3
capacity = 50
values = [60, 100, 120]
weights = [20, 50, 30]
addList = []
result = 0


for x in values:
    newVal = x / weights[values.index(x)]
    addList.append(newVal)
    
maxValIndex = addList.index(max(addList)) #remember this is already an index
#going to have to do a nested loop here
#probably something like while capacity >0



if capacity - weights[maxValIndex] >= 0:
    result = result + values[maxValIndex]
    capacity = capacity - weights[maxValIndex]
    addList[maxValIndex] = 0
    
#if capacity - weights[addList.index(maxVal)] >= 0:
#    result = result + values[maxVal]
#    capacity = capacity - weights[maxVal]
#    addList[addList.index(maxVal)] = 0
#    