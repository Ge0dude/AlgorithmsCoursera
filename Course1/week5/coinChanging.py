#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 17:41:48 2017

@author: brendontucker

using this as an example to better understand dynamic programming
"""

coinValueList = [1, 5, 21, 25]
change = 63
minCoins = [0 for x in range(change + 1)]

for cents in range(10):#(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount