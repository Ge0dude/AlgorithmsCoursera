#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:21:22 2017

@author: brendontucker
"""
import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course2/week1/checkBracketTest5')
sys.stdin = file

def testFunc(stringPlz):    
    openList = []
    counter1 = 0
    for x in stringPlz:
#        if x == '(' or x == '[' or x == '{':
#            if counter1 == len(stringPlz) - 1:
#                return counter1 + 1
#            else:
#                openList.append(x)
        
        if x == '(' or x == '[' or x == '{':
            #openList.insert(0,x)
            openList.append(x)
        
        if x == ')' or x == ']' or x == '}':
            if len(openList) == 0:
                return counter1 + 1
            else:
                #top = openList.pop(0)
                top = openList.pop(-1)
                if top == '(' and x != ')' or top == '[' and x != ']' or \
                top == '{' and x != '}':
                    return counter1 + 1
                    
        if counter1 == len(text) - 1:
            #print('got to the end')
            if len(openList) == 0:
                return 'Success'
            else:
                return counter1 #+ 1
                
        counter1 += 1

if __name__ == "__main__":
    text = sys.stdin.read()

    print(testFunc(text))


 
    
#def testFunc(stringPlz):    
#    openList = []
#    for x in stringPlz:
#        if x == '(' or x == '[' or x == '{':
#            openList.insert(0,x)
#        
#        if x == ')' or x == ']' or x == '}':
#            if len(openList) == 0:
#                return stringPlz.index(x) + 1
#            else:
#                top = openList.pop(0)
#                if top == '(' and x != ')' or top == '[' and x != ']' or \
#                top == '{' and x != '}':
#                    return stringPlz.index(x) + 1
#                    
#        if text.index(x) == len(text) - 1:
#            #print(openList)
#            if len(openList) == 0:
#                print('Success')
#            else: #find the last opened bracket? not sure here
#                print("Entered the last loop")
#                counter = len(stringPlz) - 1
#                print('counter value is:', counter)
#                while counter >= 0:
#                    print('value to check is:', stringPlz[counter])
#                    if stringPlz[counter] == '(' or stringPlz[counter] == '[' \
#                    or stringPlz[counter] == '{':
#                        #print('stringPlz[counter] is == to one of the three')
#                        print(stringPlz.index(stringPlz[counter]) + 1)
#                        break
#                    counter -= 1
#                    
#testFunc(text)                         
        
        
#                counter = len(stringPlz) - 1
#                while counter >= 0:
#                    if stringPlz[counter] == '(' or stringPlz[counter] == '[' \
#                    or stringPlz[counter] == '{':
#                        return(stringPlz.index(stringPlz[counter]) + 1)
#                        break
#                    counter -= 1        
        
        