# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 00:28:09 2024

@author: 86137
"""

import heapq
start = []
heapq.heapify(start)
n = int(input())
for _ in range(n):
    order = input()
    if order[0] == '1':
        heapq.heappush(start, int(order[2:]))
    elif order[0] == '2':
        print(heapq.heappop(start))
        