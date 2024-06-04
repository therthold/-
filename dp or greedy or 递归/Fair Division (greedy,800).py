# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:10:57 2024

@author: 86137
"""

t = int(input())
for _ in range(t):
    n = int(input())
    candy = list(map(int,input().split()))
    diff = 0
    candy.sort(reverse=True)
    for c in candy:
        if diff <= 0:
            diff += c
        else:
            diff -= c
    print(['NO','YES'][diff == 0])