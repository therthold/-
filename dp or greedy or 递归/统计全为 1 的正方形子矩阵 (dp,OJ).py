# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:46:08 2024

@author: 86137
"""

m,n = map(int,input().split())
marix = []
dp = []
flag = []
for _ in range(m):
    marix.append(list(map(int,input())))
    dp.append([0]*n)
    flag.append([0]*n)
for i in range(m):
    for j in range(n):
        if i == 0:
            flag[i][j] = marix[i][j]
            dp[i][j] = dp[i][j-1] + marix[i][j]
        elif j == 0:
            flag[i][j] = marix[i][j]
            dp[i][j] = dp[i-1][j] + marix[i][j]
        else:
            if flag[i-1][j] == flag[i][j-1]:
                flag[i][j] = marix[i][j]*(flag[i-1][j]+marix[i-flag[i-1][j]][j-flag[i-1][j]])
            else:
                flag[i][j] = marix[i][j]*(min(flag[i-1][j],flag[i][j-1])+1)
            dp[i][j] = dp[i][j-1] + dp[i-1][j] + flag[i][j] - dp[i-1][j-1]
print(dp[-1][-1])