# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:20:29 2024

@author: 86137
"""

n,k = map(int,input().split())
numlist = list(map(int,input().split()))
numlist.sort()
if k == 0:
    print([1,-1][numlist[0] == 1])
elif k == n:
    print(numlist[-1])
else:
    print([numlist[k-1],-1][numlist[k-1] == numlist[k]])
