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


capacityList = [[50], [10]]
valuesList = [[60, 100, 120], [500]]
weightsList = [[20, 50, 30], [30]]


capacity = capacityList[0][0]
values = valuesList[0]
weights = weightsList[0]
n = 3
addList = []
result = 0

if type(values) == list:
    for x in values:
        newVal = x / weights[values.index(x)]
        addList.append(newVal)
#if type(values) == int:
#    addList.append(values/weights)
    

while capacity > 0:
    maxVal = max(addList)
    if maxVal > 0: 
        maxValIndex = addList.index(max(addList))
        if capacity - weights[maxValIndex] >= 0:
            result = result + values[maxValIndex]
            capacity = capacity - weights[maxValIndex]
            addList[maxValIndex] = 0
        else:
            fraction = capacity / weights[maxValIndex] 
            result = result + (values[maxValIndex] * fraction)
            capacity = capacity - (weights[maxValIndex] * fraction)
            
        
        
        

    
#if capacity - weights[addList.index(maxVal)] >= 0:
#    result = result + values[maxVal]
#    capacity = capacity - weights[maxVal]
#    addList[addList.index(maxVal)] = 0
#    


#maxValIndex = addList.index(max(addList)) #remember this is already an index
##going to have to do a nested loop here
##probably something like while capacity >0



#doesn't allow for fractional partitions yet
#didn't exit the loop... hmm
