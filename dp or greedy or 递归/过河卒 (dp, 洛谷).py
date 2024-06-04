# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:32:24 2024

@author: 86137
"""

end_i, end_j, ban_i, ban_j = map(int,input().split())
ban = {(ban_i, ban_j):1, (ban_i-1, ban_j-2):1, (ban_i-1, ban_j+2):1, (ban_i+1, ban_j-2):1, (ban_i+1, ban_j+2):1, 
       (ban_i-2, ban_j-1):1, (ban_i-2, ban_j+1):1, (ban_i+2, ban_j-1):1, (ban_i+2, ban_j+1):1}
dp = []
for i in range(end_i+1):
    dp.append([1]*(end_j+1))
    for j in range(end_j+1):
        if (i, j) in ban:
            dp[i][j] = 0
        elif i == 0 and j == 0:
            dp[i][j] = 1
        elif i == 0:
            dp[i][j] = dp[i][j-1]
        elif j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[end_i][end_j])