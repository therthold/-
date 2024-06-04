# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:45:16 2024

@author: 86137
"""
from heapq import *

def prim(codes):
    result, cost = 0, [float('inf')]*len(codes)
    queue, visited = [(0,0)], [0]*len(codes)
    heapify(queue)
    cost[0] = 0
    while queue:
        cur_cost, cur = heappop(queue)
        if visited[cur]:
            continue
        result += cur_cost
        visited[cur] = 1
        for idx in range(len(codes)):
            if not visited[idx] and not idx == cur:
                new_cost = distance(codes[cur], codes[idx])
                if cost[idx] > new_cost:
                    cost[idx] = new_cost
                    heappush(queue, (cost[idx], idx))
    return result

def distance(code1, code2):
    result = 0
    for idx in range(len(code1)):
        result += not code1[idx] == code2[idx]
    return result

while True:
    N = int(input())
    if not N:
        break
    codes = []
    for _ in range(N):
        codes.append(input())
    print('The highest possible quality is 1/%s.'%(prim(codes)))