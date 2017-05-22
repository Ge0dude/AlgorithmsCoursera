#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 07:42:25 2017

@author: brendontucker
"""

W = 10 
n = 3
wt = [1, 4, 8]

K = [[0 for x in range(W+1)] for x in range(n+1)]

for i in range(n+1):
    for w in range(W+1):
        if i==0 or w==0:
            K[i][w] = 0
        elif wt[i-1] <= w:
            K[i][w] = max(wt[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
        else:
            K[i][w] = K[i-1][w]