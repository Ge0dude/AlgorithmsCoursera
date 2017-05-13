#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:27:24 2017

@author: brendontucker
"""
import sys
#m = 5
m = int(sys.stdin.read())
oneCount = 0
fiveCount = 0
tenCount = 0

while m - 10 >= 0:
    tenCount += 1
    m = m - 10
while m - 5 >= 0:
    fiveCount += 1
    m = m - 5
while m - 1 >= 0:
    oneCount += 1
    m = m - 1
    
result = oneCount + fiveCount + tenCount
print(result)