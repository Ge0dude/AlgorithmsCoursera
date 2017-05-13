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




capacity = 10
values = [5]
weights = [30]
n = 1
addList = []
result = 0


addList = []
result = 0

for x in values:
    newVal = x / weights[values.index(x)]
    addList.append(newVal)


while capacity > 0:
    maxVal = max(addList)
    if maxVal > 0: 
        maxValIndex = addList.index(max(addList))
        if weights[maxValIndex] <= capacity:# >= 0:
            result = result + values[maxValIndex]
            addList[maxValIndex] = 0
            capacity = capacity - weights[maxValIndex]
        else:
            fraction = capacity / weights[maxValIndex]
            result = result + (values[maxValIndex] * fraction)
            addList[maxValIndex] = addList[maxValIndex] - (addList[maxValIndex] * fraction)
            capacity = capacity - (weights[maxValIndex] * fraction)
    elif maxVal == 0:
        break
        
        
        

    

