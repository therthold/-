# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:24:55 2024

@author: 86137
"""

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    dp = [0]*n
    if n == 1:
        print('First')
    else:
        for i in range(n):
            if i == 0:
                dp[i] = ['First','Second'][num[0] > 1]
            elif i == n-1:
                dp[i] = ['First','Second'][dp[i-1] == 'First']
            else:
                dp[i] = ['First','Second'][((dp[i-1] == 'First') + (num[i] > 1 and num[i+1] > 1))%2]
        print(['First','Second'][dp[-1] == 'Second'])
            
    