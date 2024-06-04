# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:16:11 2024

@author: 86137
"""

s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
dp = [[0]*(l2) for _ in range(l1)]
for i in range(l1):
    for j in range(l2):
        if i == 0:
            if s1[i] == s2[j]:
                dp[i][j] = 1
        elif j == 0:
            if s1[i] == s2[j]:
                dp[i][j] = 1
        else:
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[l1-1][l2-1])