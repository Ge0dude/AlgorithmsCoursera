#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:38:16 2017

@author: brendontucker
"""

import sys

file = open('/Users/brendontucker/AlgorithmsCoursera/Course1/week3/fractionalTest1')
sys.stdin = file

data = list(map(int, sys.stdin.read().split()))
n, capacity = data[0:2]
values = data[2:(2 * n + 2):2]
weights = data[3:(2 * n + 2):2]