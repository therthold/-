# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:49:56 2024

@author: 86137
"""

n = int(input())
dp = []
plan = []
for _ in range(n):
    dp.append([0]*45)
    start, end, value = map(str,input().split())
    start = int(start[0])*31 + int(start[2:]) - 38 ## 日期的映射，对应着0-44
    end = int(end[0])*31 + int(end[2:]) - 38
    plan.append([start,end,int(value)])
plan.sort()
for i in range(n):
    for j in range(45):
        if plan[i][1] > j:
            dp[i][j] = dp[i-1][j]
        elif plan[i][0] == 0:
            dp[i][j] = max(dp[i-1][j], plan[i][2])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][plan[i][0]-1] + plan[i][2])
print(dp[-1][-1])
        