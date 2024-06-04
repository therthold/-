# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:35:09 2024

@author: 86137
"""

apple, num = map(int,input().split())
dp = []
for _ in range(num + 1):
    dp.append([0]*(apple + 1))
for i in range(num + 1):
    for j in range(apple + 1):
        if i <= 1 or j <= 1:
            dp[i][j] = 1
        else:
            time = 0
            while j-time*i >= 0:
                dp[i][j] += dp[i-1][j-time*i]
                time += 1
print(dp[-1][-1])