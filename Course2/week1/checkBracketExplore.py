#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:21:22 2017

@author: brendontucker
"""
import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course2/week1/checkBracketTest1')
sys.stdin = file

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            pass

    # Printing answer, write your code here


def testFunc(stringPlz):    
    openList = []
    #clostList = []
    for x in stringPlz:
        if x == '(' or x == '[' or x == '{':
            openList.insert(0,x)
        
        if x == ')' or x == ']' or x == '}':
            if len(openList) == 0:
                return stringPlz.index(x)
            else:
                top = openList.pop(0)
                if top == '(' and x != ')' or top == '[' and x != ']' or \
                top == '{' and x != '}':
                    return stringPlz.index(x)
                    
                    
                
            
        
        
        
        
        
        