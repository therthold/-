# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:02:05 2024

@author: 86137
"""
## ---.--.-..
## -..-.-....
## ...--....-
## ----......
## --.---....
## -.-..-.---
## ....-.-..-
## -..-----..
## -.......-.
## .....--.--
## 8

def check(Map, i, j):
    if i < 0 or j < 0 or i >= len(Map) or j >= len(Map[0]) or Map[i][j] == '-':
        return False
    else:
        return True

def dfs(Map, i, j, S, move = [(1,0),(-1,0),(0,1),(0,-1)]):
    if check(Map, i, j):
        if Map[i][j] == '.':
            S += 1
            Map[i][j] = '-'
            for m in move:
                S = dfs(Map, i + m[0], j + m[1], S)
    return S

Map = []
for _ in range(10):
    Map.append(list(input()))
result = 0
for i in range(10):
    for j in range(10):
        result += (dfs(Map, i, j, 0) > 0)
print(result)
            
        
    