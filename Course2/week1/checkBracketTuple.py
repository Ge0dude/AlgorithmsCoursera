#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:50:20 2017

@author: brendontucker
"""

import sys

#file = open('/Users/brendontucker/AlgorithmsCoursera/Course2/week1/checkBracketTest4')
#sys.stdin = file


def testFunc(stringPlz):
    openList = []
    #posList = []
    counter1 = 0
    for x in stringPlz:
        if x == '(' or x == '[' or x == '{':
            if counter1 == len(stringPlz) - 1:
                return counter1 + 1
            else:
                openList.append(x)
                #openList.insert(0,x)
        
        if x == ')' or x == ']' or x == '}':
            #print(openList)
            if len(openList) == 0:
                return counter1 + 1
            else:
                top = openList.pop(-1)
                if top == '(' and x != ')' or top == '[' and x != ']' or \
                top == '{' and x != '}':
                    return counter1 + 1
                    
        if counter1 == len(stringPlz) - 1:
            if len(openList) == 0:
                return 'Success'
        
        counter1 += 1

if __name__ == "__main__":
    text = sys.stdin.read()
    if len(text) == 1:
        print(1)
    else:
        print(testFunc(text))
    

    
    
