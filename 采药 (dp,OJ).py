# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:41:44 2024

@author: 86137
"""

t,m = map(int,input().split())
dp = []
herb = []
for _ in range(m):
    dp.append([0]*(t+1))
    time,value = map(int,input().split())
    herb.append([value,time])
for i in range(m):
    for j in range(t+1):
        if herb[i][1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-herb[i][1]]+herb[i][0])
print(dp[-1][-1])