# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:20:56 2024

@author: 86137
"""
import heapq

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
    
    def addEdge(self, fr, to, weight):
        if fr not in self.ids:
            self.addVertex(fr)
        if to not in self.ids:
            self.addVertex(to)
        self.ids[fr].addneigh(to, weight)

def Prim(graph, start):
    queue = [(0, start)]
    heapq.heapify(queue)
    visited = set()
    result = 0
    while queue:
        weight, cur = heapq.heappop(queue)
        if cur in visited:
            continue
        result += weight
        visited.add(cur)
        for c in graph.ids[cur].connection:
            if not c in visited:
                w = graph.ids[cur].connection[c]
                heapq.heappush(queue, (w, c))
    return result

while True:
    try:
        N = int(input())
        graph = Graph()
        start = 0
        record = float('inf')
        for idx in range(N):
            weights = list(map(int,input().split()))
            if not len(weights) == N:
                weights += list(map(int,input().split()))
            for j in range(idx+1, N):
                if weights[j] < record:
                    record = weights[j]
                    start = idx
                graph.addEdge(idx, j, weights[j])
                graph.addEdge(j, idx, weights[j])
        print(Prim(graph, start))
    except EOFError:
        break


        