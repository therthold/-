# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:10:10 2024

@author: 86137
"""

n = int(input())
hig = list(map(int,input().split()))
dp = [1]*n
result = 0
for i in range(n-2,-1,-1):
    for j in range(i+1, n):
        if hig[i] >= hig[j]:
            dp[i] = max(dp[i], dp[j]+1)
    result = max(result, dp[i])
print(result)