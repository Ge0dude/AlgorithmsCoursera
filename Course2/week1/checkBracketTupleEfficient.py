#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:39:57 2017

@author: brendontucker
"""

import sys

#file = open('/Users/brendontucker/AlgorithmsCoursera/Course2/week1/checkBracketTest1')
#sys.stdin = file


#def testFunc(text):    
#    openList = []
#    posList = []
#    counter1 = 0
#    for i, next in enumerate(text):
#        if next == '(' or next == '[' or next == '{':
#            if counter1 == len(text) - 1:
#                return counter1 + 1
#            else:
#                openList.insert(0,next)
#                posList.insert(0,counter1)
#                #print(posList)
#            
#
#
#        if next == ')' or next == ']' or next == '}':
#            if len(openList) == 0:
#                return counter1 + 1
#            else:
#                #print(openList)
#                top = openList.pop(0)
#                #print('top =', top)
#                #print(posList)
#                topIn = posList.pop(0) #dont' have to assign here
#                #print('topIn =', topIn)
#                if top == '(' and next != ')' or top == '[' and next != ']' or \
#                top == '{' and next != '}':
#                    return counter1 + 1
#                    
#                    
#        if counter1 == len(text) - 1:
#            if len(openList) == 0:
#                return 'Success'
#            else:
#                #print(openList)
#                topAgain = posList[0]
#                return topAgain + 1
#                
#        counter1 += 1
#        
#if __name__ == "__main__":
#    text = sys.stdin.read()
#
#    print(testFunc(text))

        
        
if __name__ == "__main__":
    text = sys.stdin.read()

    openList = []
    posList = []
    counter1 = 0
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            if counter1 == len(text) - 1:
                print( counter1 + 1)
                break
            else:
                openList.insert(0,next)
                posList.insert(0,counter1)
                #print(posList)
            


        if next == ')' or next == ']' or next == '}':
            if len(openList) == 0:
                print( counter1 + 1)
                break
            else:
                #print(openList)
                top = openList.pop(0)
                #print('top =', top)
                #print(posList)
                topIn = posList.pop(0)
                #print('topIn =', topIn)
                if top == '(' and next != ')' or top == '[' and next != ']' or \
                top == '{' and next != '}':
                    print( counter1 + 1)
                    break
                    
                    
        if counter1 == len(text) - 1:
            if len(openList) == 0:
                print( 'Success')
                break
            else:
                #print(openList)
                topAgain = posList[0]
                print( topAgain + 1)
                break
        counter1 += 1
        
        



#def testFunc(stringPlz):    
#    openList = []
#    posList = []
#    counter1 = 0
#    for x in stringPlz:
#        
#        if x == '(' or x == '[' or x == '{':
#            if counter1 == len(text) - 1:
#                return counter1 + 1
#            else:
#                openList.insert(0,x)
#                posList.insert(0,counter1)
#                #print(posList)
#        
#        if x == ')' or x == ']' or x == '}':
#            #print(openList)
#            if len(openList) == 0:
#                return counter1 + 1
#            else:
#                #print(openList)
#                top = openList.pop(0)
#                #print('top =', top)
#                #print(posList)
#                topIn = posList.pop(0)
#                #print('topIn =', topIn)
#                if top == '(' and x != ')' or top == '[' and x != ']' or \
#                top == '{' and x != '}':
#                    return counter1 + 1
#                    
#        if counter1 == len(text) - 1:
#            if len(openList) == 0:
#                return 'Success'
#            else:
#                #print(openList)
#                topAgain = posList[0]
#                return topAgain + 1
#        counter1 += 1        
        
        
#if __name__ == "__main__":
#    text = sys.stdin.read()
#
#    print(testFunc(text))