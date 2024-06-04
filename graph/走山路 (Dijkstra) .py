# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 10:04:04 2024

@author: 86137
"""

import heapq
def check(Map, i, j, visited):
    if i < 0 or j < 0 or i >= len(Map) or j >= len(Map[0]):
        return False
    if (i, j) in visited or Map[i][j] == '#':
        return False
    else:
        return True

def Dijkstra(Map, start_i, start_j, end_i, end_j):
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = [(0, start_i, start_j)]
    heapq.heapify(queue)
    visited = set()
    while not queue == []:
        path, cur_i, cur_j = heapq.heappop(queue)
        if cur_i == end_i and cur_j == end_j:
            return path
        if (cur_i, cur_j) in visited:
            continue
        visited.add((cur_i, cur_j))
        for m in move:
            i, j = cur_i + m[0], cur_j + m[1]
            if check(Map, i, j, visited):
                new_path = path + abs(int(Map[i][j]) - int(Map[cur_i][cur_j]))
                heapq.heappush(queue, (new_path, i, j))
    return 'NO'

m, n, p = map(int,input().split())
Map= []
f_result = []
for _ in range(m):
    Map.append(input().split())
for _ in range(p):
    start_i, start_j, end_i, end_j = map(int,input().split())
    if Map[start_i][start_j] == '#' or Map[end_i][end_j] == '#':
        result = 'NO'
    else:
        result = Dijkstra(Map, start_i, start_j, end_i, end_j)
    print(result)
