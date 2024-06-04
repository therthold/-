# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:54:38 2024

@author: 86137
"""
import heapq

class Vertex:
    def __init__(self, val):
        self.val = val
        self.connection = {}
    def add(self, item, weight):
        self.connection[item] = weight

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
        self.ids[fr].add(to, weight)

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

n = int(input())
graph = Graph()
record = float('inf')
for _ in range(n-1):
    keylist = input().split()
    val = keylist[0]
    num = int(keylist[1])
    for idx in range(num):
        weight = int(keylist.pop())
        if weight < record:
            start = val
        target = keylist.pop()
        graph.addEdge(val, target, weight)
        graph.addEdge(target, val, weight)
print(Prim(graph, start))




            