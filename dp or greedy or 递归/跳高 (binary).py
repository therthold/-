# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:47:06 2024

@author: 86137
"""
from bisect import *

cur_temps = []
N = int(input())
scores = list(map(int,input().split()))
for idx in range(N):
    cur = scores[idx]
    if cur_temps:
        if cur >= cur_temps[-1]:
            cur_temps[-1] = cur
        else:
            ind = bisect(cur_temps, cur)
            if ind == 0:
                cur_temps.insert(0, cur)
            else:
                cur_temps[ind - 1] = cur
    else:
        cur_temps.append(cur)
print(len(cur_temps))
    

    