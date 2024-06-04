# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 19:49:25 2024

@author: 86137
"""

def findmax(L, idx):
    result = 1
    for i in range(idx+1, len(L)):
        if L[idx] >= L[i]:
            result = max(result, findmax(L, i)+1)
    return result

n = int(input())
hig = list(map(int,input().split()))
result = 0
for i in range(n):
    result = max(result, findmax(hig, i))
print(result)