# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:59:25 2024

@author: 86137
"""
import math
t = int(input())
for _ in range(t):
    n = int(input())
    maxH = math.floor((math.sqrt(1+16*n)-1)/4)
    if n == 1:
        print(0)
    else:
        dp = [1]*maxH
        for i in range(maxH-1,-1,-1):
            if i == maxH-1:
                dp[i] = n//((3*i+4)*(i+1)//2)
            else:
                dp[i] = n//((3*i+4)*(i+1)//2) + dp[i+1]
            n = n%((3*i+4)*(i+1)//2)
        print(dp[0])
    
        