#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:10:09 2017

@author: brendontucker
"""

import sys

#file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week3/dotProductTest1')
#sys.stdin = file

def max_dot_product(a, b):
    #write your code here
    res = 0
    a.sort()
    b.sort()
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))