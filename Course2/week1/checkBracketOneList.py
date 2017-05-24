#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 07:33:48 2017

@author: brendontucker
"""

import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course2/week1/checkBracketTest4')
sys.stdin = file

        
        
if __name__ == "__main__":
    text = sys.stdin.read()

    openList = []
    counter1 = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            if counter1 == len(text) - 1:
                print(counter1 + 1)
                break
            else:
                openList.insert(0,next)
            


        if next == ')' or next == ']' or next == '}':
            if len(openList) == 0:
                print(counter1 + 1)
                break
            else:
                top = openList.pop(0)
                if top == '(' and next != ')' or top == '[' and next != ']' or \
                top == '{' and next != '}':
                    print(counter1 + 1)
                    break
                    
                    
        if counter1 == len(text) - 1:
            if len(openList) == 0:
                print( 'Success')
                break
        counter1 += 1