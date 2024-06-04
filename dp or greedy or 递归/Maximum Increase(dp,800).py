# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:18:36 2024

@author: 86137
"""

n = int(input())
num = list(map(int,input().split()))
dp = [1]*n
result = 1
for i in range(1,n):
    if num[i] > num[i-1]:
        dp[i] = max(dp[i], dp[i-1]+1)
    result = max(result, dp[i])
print(result)