# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:16:23 2024

@author: 86137
"""

import heapq
T = int(input())
for _ in range(T):
    result = []
    data = list(map(int,input().split()))
    cur = float('-inf')
    cur_small = []
    cur_large = []
    heapq.heapify(cur_small)
    heapq.heapify(cur_large)
    for idx in range(len(data)):
        if data[idx] >= cur:
            heapq.heappush(cur_large, data[idx])
        else:
            heapq.heappush(cur_small, -data[idx])
        
        if len(cur_large) > len(cur_small):
            cur = heapq.heappop(cur_large)
            if idx%2 == 0:
                result.append(str(cur))
            heapq.heappush(cur_small, -cur)
        elif len(cur_large) < len(cur_small):
            cur = -heapq.heappop(cur_small)
            if idx%2 == 0:
                result.append(str(cur))
            heapq.heappush(cur_large, cur)
    print((len(data)+1)//2)
    print(' '.join(result))
    