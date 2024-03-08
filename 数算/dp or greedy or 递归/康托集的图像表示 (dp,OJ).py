# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 09:10:27 2024

@author: 86137
"""

n = int(input())
dp = ['']*n
for i in range(n):
    if i == 0:
        dp[i] = '*-*'
    else:
        dp[i] = dp[i-1] + '-'*(3**i) + dp[i-1]
print(dp[-1])