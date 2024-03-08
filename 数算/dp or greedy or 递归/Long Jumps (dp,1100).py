# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:35:25 2024

@author: 86137
"""

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    dp = [0]*n
    result = 0
    for i in range(n-1,-1,-1):
        if i + num[i] >= n:
            dp[i] = num[i]
        else:
            dp[i] = dp[i+num[i]] + num[i]
        result = max(result, dp[i])
    print(result)
        