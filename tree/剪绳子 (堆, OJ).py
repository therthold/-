# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:23:40 2024

@author: 86137
"""

import heapq

n = int(input())
ropes = list(map(int,input().split()))
heapq.heapify(ropes)
result = 0
while len(ropes) > 1:
    new_rope = heapq.heappop(ropes) + heapq.heappop(ropes)
    result += new_rope
    heapq.heappush(ropes, new_rope)
print(result)
