# -*- coding: utf-8 -*-
"""
Created on Wed May  1 20:03:10 2024

@author: 86137
"""

def bfs(A, B, C):
    queue = [(0, 0, [])]
    visited = {}
    while queue:
        cur_A, cur_B, path = queue.pop(0)
        if cur_A == C or cur_B == C:
            return path
        if (A, cur_B) not in visited:
            queue.append((A, cur_B, path + ['FILL(1)']))
            visited[(A, cur_B)] = 0
        if (cur_A, B) not in visited:
            queue.append((cur_A, B, path + ['FILL(2)']))
            visited[(cur_A, B)] = 0
        if (0, cur_B) not in visited:
            queue.append((0, cur_B, path + ['DROP(1)']))
            visited[(0, cur_B)] = 0
        if (cur_A, 0) not in visited:
            queue.append((cur_A, 0, path + ['DROP(2)']))
            visited[(cur_A, 0)] = 0
        if (min(A, cur_A + cur_B), max(0, cur_A + cur_B - A)) not in visited:
            queue.append((min(A, cur_A + cur_B), max(0, cur_A + cur_B - A), path + ['POUR(2,1)']))
            visited[(min(A, cur_A + cur_B), max(0, cur_A + cur_B - A))] = 0
        if (max(0, cur_A + cur_B - B), min(B, cur_A + cur_B)) not in visited:
            queue.append((max(0, cur_A + cur_B - B), min(B, cur_A + cur_B), path + ['POUR(1,2)']))
            visited[(max(0, cur_A + cur_B - B), min(B, cur_A + cur_B))] = 0

A, B, C = map(int,input().split())
result = bfs(A, B, C)
if result == None:
    print('impossible')
else: 
    print(len(result))
    print('\n'.join(result))