#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 07:07:14 2017

@author: brendontucker
"""

def efficientGCD(a,b):
    if b == 0:
        return a
    else:
        aPrime = a % b
        return efficientGCD(b, aPrime)
        
print(efficientGCD(28851538, 1183019))