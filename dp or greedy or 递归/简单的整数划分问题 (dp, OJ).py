# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:00:04 2024

@author: 86137
"""
while True:
    try:
        N = int(input())
        dp = []
        for i in range(1+N):
            dp.append([0]*(1+N))
            for j in range(1,1+N):
                if i == 0:
                    dp[i][j] = 1
                elif i < j:
                    dp[i][j] = dp[i][i]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - j][j]
        print(dp[-1][-1])
    except EOFError:
        break
