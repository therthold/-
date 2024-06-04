# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:14:05 2024

@author: 86137
"""
from heapq import *

N, E = map(int, input().split())
in_degrees = [0]*(N+1)
edges = {i+1:[] for i in range(N)}
for _ in range(E):
    fr, to = map(int, input().split())
    edges[fr].append(to)
    in_degrees[to] += 1
queue = []
result = []
for idx in range(1,N+1):
    if in_degrees[idx] == 0:
        queue.append(idx)
heapify(queue)
while queue:
    cur = heappop(queue)
    result.append(str(cur))
    for n in edges[cur]:
        in_degrees[n] -= 1
        if in_degrees[n] == 0:
            heappush(queue, n)
print('v' + ' v'.join(result))