#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:41:48 2017

@author: brendontucker

using this as an example to better understand dynamic programming
lets do some debugging with print statements
"""

coinValueList = [1, 5, 21, 25]
change = 63
minCoins = [0 for x in range(change + 1)]

for cents in range(change+1):
    print('START LOOP')
    print('_________')
    print('cents is:', cents)
    coinCount = cents
    print('so is coinCount:', coinCount)
    for j in [c for c in coinValueList if c <= cents]:
        print('j is:', j)
        if minCoins[cents-j] + 1 < coinCount:
             coinCount = minCoins[cents-j] + 1
             print('coinCount is now:', coinCount)
    minCoins[cents] = coinCount
    print('the answer is:', coinCount)
      
#need to understand this line better

#[c for c in coinValueList if c <= cents]
'''creates a list of every coin <= cents'''

