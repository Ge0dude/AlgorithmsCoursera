#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:50:20 2017

@author: brendontucker
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:21:22 2017

@author: brendontucker
"""
import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course2/week1/checkBracketTest3')
sys.stdin = file

def testFunc(stringPlz):    
    openList = []
    posList = []
    counter1 = 0
    for x in stringPlz:
        
        if x == '(' or x == '[' or x == '{':
            openList.insert(0,x)
            posList.insert(0,counter1)
            print(posList)
        
        if x == ')' or x == ']' or x == '}':
            #print(openList)
            if len(openList) == 0:
                return counter1 + 1
            else:
                top = openList.pop(0)
                if top == '(' and x != ')' or top == '[' and x != ']' or \
                top == '{' and x != '}':
                    return counter1 + 1
                    
        if counter1 == len(text) - 1:
            if len(openList) == 0:
                return 'Success'
            else:
                #print(openList)
                topAgain = openList[0]
                return stringPlz.index(topAgain) + 1
        counter1 += 1

if __name__ == "__main__":
    text = sys.stdin.read()

    print(testFunc(text))