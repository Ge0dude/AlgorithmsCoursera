#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:00:32 2017

@author: brendontucker
"""
import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week4/majorityTest1')
sys.stdin = file

#def get_majority_element(a, left, right):
#    if left == right:
#        return -1
#    if left + 1 == right:
#        return a[left]
#    #write your code here
#    return -1



#if __name__ == '__main__':
#    input = sys.stdin.read()
#    n, *a = list(map(int, input.split()))
#    if get_majority_element(a, 0, n) != -1:
#        print(1)
#    else:
#        print(0)

input = sys.stdin.read()
n, *a = list(map(int, input.split()))

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
        