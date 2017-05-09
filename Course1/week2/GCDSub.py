#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 07:18:00 2017

@author: brendontucker
"""
import sys

def efficientGCD(a,b):
    if b == 0:
        return a
    else:
        aPrime = a % b
        return efficientGCD(b, aPrime)
        
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(efficientGCD(a, b))