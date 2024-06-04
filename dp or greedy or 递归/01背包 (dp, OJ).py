# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:02:02 2024

@author: 86137
"""

N,M = map(int,input().split())
dp = [0]*(M+1)
for i in range(N):
    need, value = map(int,input().split())
    for j in range(M, need-1, -1):
        dp[j] = max(dp[j], dp[j - need] + value)
print(dp[-1])