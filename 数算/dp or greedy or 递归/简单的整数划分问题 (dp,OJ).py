# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:50:33 2024

@author: 86137
"""
while True:
    try:
        n = int(input())
        dp = []
        for _ in range(n + 1):
            dp.append([0]*(n + 1))
        for i in range(n + 1):
            for j in range(n + 1):
                if i <= 1 or j <= 1:
                    dp[i][j] = 1
                else:
                    time = 0
                    while j-time*i >= 0:
                        dp[i][j] += dp[i-1][j-time*i]
                        time += 1
        print(dp[-1][-1])   
    except EOFError:
        break
