# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:48:17 2024

@author: 86137
"""

N = int(input())
files = {}
for i in range(N):
    f = list(map(int,input().split()))[1:]
    for j in range(len(f)):
        if f[j] not in files:
            files[f[j]] = [-1]*N
        files[f[j]][i] = 1
M = int(input())
for _ in range(M):
    result = []
    search = list(map(int,input().split()))
    for f in files:
        if all(x*y >= 0 for x, y in zip(search, files[f])):
            result.append(str(f))
    if result == []:
        print('NOT FOUND')
    else:
        result.sort(key=lambda x:int(x))
        print(' '.join(result))
    
        
