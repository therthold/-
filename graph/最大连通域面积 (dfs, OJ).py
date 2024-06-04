# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:13:17 2024

@author: 86137
"""

def dfs(i, j, matrix, S, move):
    rowmax = len(matrix)
    colmax = len(matrix[0])
    if i >= rowmax or i < 0 or j >= colmax or j < 0:
        return S
    elif matrix[i][j] == '.':
        return S
    else:
        matrix[i][j] = '.' #直接把他变为.以防止回溯
        S += 1
        for m in move:
            S = dfs(i+m[0], j+m[1], matrix, S, move)
        return S

move = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
T = int(input())
for _ in range(T):
    matrix = []
    N,M = map(int,input().split())
    s = 0
    for row in range(N):
        matrix.append(list(map(str,input())))
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                S = dfs(i, j, matrix, 0, move)
                s = max(s, S)
    print(s)