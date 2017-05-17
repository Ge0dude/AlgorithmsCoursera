#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:00:32 2017

@author: brendontucker

error is likely whether I initialize i = 1 upon changing m, and then how j
is treated 
"""
import sys

#file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/majorityTest2')
#sys.stdin = file

def get_majority_element(array1, length):
    candidate = 0
    count = 0
    for value in array1:
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
    if j/length > 1/2:
        ans = 1
        
    return ans



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, n))



  