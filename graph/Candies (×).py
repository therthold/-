# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:20:26 2024

@author: 86137
"""

import heapq
class Vertex():
    def __init__(self, val):
        self.val = val
        self.neigh = {}
    
    def addneigh(self, val, weight):
        self.neigh[val] = weight

class Graph():
    def __init__(self):
        self.ids = {}
    
    def addVer(self, val):
        self.ids[val] = Vertex(val)
    
    def addEdge(self, fr, to, weight):
        if not fr in self.ids:
            self.addVer(fr)
        if not to in self.ids:
            self.addVer(to)
        self.ids[fr].addneigh(to, weight)

def findmax(graph, start, end):
    queue = [(0, start)]
    visited = {start:0}
    heapq.heapify(queue)
    while queue:
        value, ids = heapq.heappop(queue)
        if ids == end:
            return value
        cur = graph.ids[ids]
        for neigh in cur.neigh:
            new_length = cur.neigh[neigh]
            if not neigh in visited or value + new_length < visited[neigh]:
                visited[neigh] = value + new_length
                heapq.heappush(queue, (value + new_length, neigh))
    
g = Graph()
n, m = map(int,input().split())
for _ in range(m):
    a, b, c = map(int,input().split())
    g.addEdge(a, b, c)
print(findmax(g, 1, n))