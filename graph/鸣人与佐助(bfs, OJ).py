# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:52:59 2024

@author: 86137
"""

def check(Map, i, j, t, visited):
    if i < 0 or j < 0 or i >= len(Map) or j >= len(Map[0]):
        return False
    elif Map[i][j] == '#' and t <= 0:
        return False
    elif i*len(Map)+j in visited and t <= visited[i*len(Map)+j]:
        return False
    else:
        return True

def bfs(Map, start, target, T):
    queue = [(0, start[0], start[1], T)]
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    visited = {start[0]*len(Map)+start[1]: 0}
    result = -1
    while not queue == []:
        length, i, j, t = queue.pop(0)
        if Map[i][j] == target:
            result = length
            break
        for m in move:
            new_i, new_j = i + m[0], j + m[1]
            if check(Map, new_i, new_j, t, visited):
                if Map[new_i][new_j] == '#':
                    new_t = t - 1
                else:
                    new_t = t
                queue.append((length + 1, new_i, new_j, new_t))
                visited[new_i*len(Map)+new_j] = new_t
    return result


M, N, T = map(int,input().split())
Map = []
for i in range(M):
    path = input()
    if '@' in path:
        start = [i, path.index('@')]
    Map.append(list(path))
print(bfs(Map, start, '+', T))
