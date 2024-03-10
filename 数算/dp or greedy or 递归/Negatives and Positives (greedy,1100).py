# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:48:57 2024

@author: 86137
"""

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    result = 0
    Min = 0
    count = 0
    for i in range(n):
        if i == 0:
            Min = abs(num[i])
        if num[i] < 0:
            count += 1
            result -= num[i]
        else:
            result += num[i]
        Min = min(Min, abs(num[i]))
    print(result - 2 * Min * (count%2 != 0))
    