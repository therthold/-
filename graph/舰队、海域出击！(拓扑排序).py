# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:23:20 2024

@author: 86137
"""
from collections import deque

class Vertex:
    def __init__(self, val):
        self.id = val
        self.connection = {}
    
    def addneigh(self, val, weight):
        self.connection[val] = weight

class Graph:
    def __init__(self):
        self.ids = {}
    
    def addVertex(self, val):
        self.ids[val] = Vertex(val)
    
    def addEdge(self, fr, to):
        if fr not in self.ids:
            self.addVertex(fr)
        if to not in self.ids:
            self.addVertex(to)
        self.ids[fr].addneigh(to, 1)

def check(graph):
    in_degree = {v: 0 for v in graph.ids}
    for up in graph.ids:
        for v in graph.ids[up].connection:
            in_degree[v] += 1
    q = deque([v for v in in_degree if in_degree[v] == 0])
    visited = []
    while q:
        cur = q.popleft()
        visited.append(cur)
        for v in graph.ids[cur].connection:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    if not len(visited) == len(graph.ids):
        return 'Yes'
    return 'No'

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    g = Graph()
    g.ids = {i:Vertex(i) for i in range(1,N+1)}
    for _ in range(M):
        i, j = map(int,input().split())
        g.addEdge(i, j)
    print(check(g))
        
    