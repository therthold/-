# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:26:32 2024

@author: 86137
"""

import heapq
N = int(input())
woods = []
for _ in range(N):
    woods.append(int(input()))
heapq.heapify(woods)
result = 0
while not len(woods) == 1:
    newwood = heapq.heappop(woods) + heapq.heappop(woods)
    result += newwood
    heapq.heappush(woods, newwood)
print(result)