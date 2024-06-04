# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:33:11 2024

@author: 86137
"""

a,n,m,x = map(int,input().split())
A = [1]*n
K = [0]*n
T = [(1,0)]*n
if x == n:
    result = 0
elif x == 1 or x == 2:
    result = a 
else:
    A[1] = 0
    K[1] = 1
    T[1] = (1,0)
    for i in range(2,n):
        A[i] = A[i-1] + A[i-2]
        K[i] = K[i-1] + K[i-2]
        cur_a, cur_k = T[i-1]
        T[i] = (cur_a + A[i-2], cur_k + K[i-2])
    k = (m - a * T[-2][0])//T[-2][1]
    result = T[x-1][0] * a + T[x-1][1] * k
print(result)