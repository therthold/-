# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:24:45 2024

@author: 86137
"""
# 6
# 321 32 407 135 13 217
# 4073232121713513

def rechange(L):
    for idx in range(len(L)-1):
        if int(L[idx] + L[idx+1]) < int(L[idx+1] + L[idx]):
            L[idx], L[idx+1] = L[idx+1], L[idx]
    return L
    
n = int(input())
L = list(map(str, input().split()))
L.sort(reverse=True)
L = rechange(L)
print(int(''.join(L)))