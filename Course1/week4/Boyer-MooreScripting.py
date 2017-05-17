#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:04:42 2017

@author: brendontucker
"""

import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/majorityTest1')
sys.stdin = file

input = sys.stdin.read()
n, *a = list(map(int, input.split()))

candidate = 0
count = 0
for value in a:
  if count == 0:
    candidate = value
  if candidate == value:
    count += 1
  else:
    count -= 1

j = 0        
for values in a:
    if values == candidate:
        j += 1

ans = 0        
if j/n > 1/2:
    ans = 1 
      
    
    
    
candidate = 0
count = 0
for value in input:
  if count == 0:
    candidate = value
  if candidate == value:
    count += 1
  else:
    count -= 1