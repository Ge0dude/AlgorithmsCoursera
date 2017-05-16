#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:00:32 2017

@author: brendontucker
"""
import sys

#file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/majorityTest1')
#sys.stdin = file

def get_majority_element(array1):
    m = 0 #element
    i = 0 #counter
    for x in a:
        if m == 0:
            m = x
            i = 1
        elif m == x:
            i += 1
        else:
            i -= 1
    
    j = 0        
    for y in a:
        if y == m:
            j += 1
    
    ans = 0        
    if j/n > 1/2:
        ans = m
        
    return ans



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a))

'''global version for testing'''

#input = sys.stdin.read()
#n, *a = list(map(int, input.split()))
#
#m = 0 #element
#i = 0 #counter
#for x in a:
#    if m == 0:
#        m = x
#        i = 1
#    elif m == x:
#        i += 1
#    else:
#        i -= 1
#
#j = 0        
#for y in a:
#    if y == m:
#        j += 1
#
#ans = 0        
#if j/n > 1/2:
#    ans = m 
#        