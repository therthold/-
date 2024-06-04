# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:25:23 2024

@author: 86137
"""

def dfs(a, b, c, i, j):
    if i == -1 and j == -1:
        return True
    if i >=0 and a[i] == c[i+j+1]:
        if dfs(a, b, c, i-1, j):
            return True
    if j >=0 and b[j] == c[i+j+1]:
        if dfs(a, b, c, i, j-1):
            return True
    return False

n = int(input())
for i in range(1,n+1):
    a,b,c = map(list,input().split())
    if dfs(a, b, c, len(a)-1, len(b)-1):
        print('Data set %s: yes'%(i))
    else:
        print('Data set %s: no'%(i))
