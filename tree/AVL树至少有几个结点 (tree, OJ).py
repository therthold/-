# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:57:09 2024

@author: 86137
"""

n = int(input())
if n == 1:
    print(1)
else:
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2] + 1
    print(dp[n])
    