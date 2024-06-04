# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:10:23 2024

@author: 86137
"""
from heapq import *

def find(graph, start, end, cost):
    queue = [(0, 0, start)]
    heapify(queue)
    while queue:
        cur_length, cur_cost, cur_city = heappop(queue)
        if cur_city == end:
            return cur_length
        for nei in graph[cur_city]:
            for value in graph[cur_city][nei]:
                add_length, add_cost = value
                if cur_cost + add_cost > cost:
                    continue
                else:
                    heappush(queue, (cur_length + add_length, cur_cost + add_cost, nei))
    return -1

max_K = int(input())
N = int(input())
Roads = int(input())
city = {i:{} for i in range(1,N+1)}
for _ in range(Roads):
    start, end, length, value = map(int,input().split())
    if end in city[start]:
        city[start][end].append((length, value))
    else:
        city[start][end] = [(length, value)]
print(find(city, 1, N, max_K))
