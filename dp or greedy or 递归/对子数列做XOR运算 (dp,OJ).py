# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:40:50 2024

@author: 86137
"""

V = list(map(int,input().split()))
dp = [0]*len(V)
for i in range(len(V)):
    if i == 0:
        dp[i] = V[i]
    else:
        dp[i] = dp[i-1]^V[i]
for i in range(10000):
    start, end = map(int,input().split())
    if start != 0:
        print(dp[end]^dp[start-1])
    else:
        print(dp[end])
    