# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:22:21 2024

@author: 86137
"""

import heapq
n = int(input())
numlist = list(map(int,input().split()))
heapq.heapify(numlist)
result = 0
while not len(numlist) == 1:
    newT = heapq.heappop(numlist)+heapq.heappop(numlist)
    result += newT
    heapq.heappush(numlist, newT)
print(result)