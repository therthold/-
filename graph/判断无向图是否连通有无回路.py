# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:52:50 2024

@author: 86137
"""

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

def check(graph, start_val, target):
    queue = [start_val]
    visited = set()
    result = [False, False]
    while queue:
        cur = queue.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for c in graph.ids[cur].connection:
            if c in queue:
                result[0] = True
            if not c in visited:
                queue.append(c)
    result[1] = len(visited) == target
    return result

n,m = map(int,input().split())
graph = Graph()
for _ in range(m):
    fr, to = map(int,input().split())
    graph.addEdge(fr, to, 0)
    graph.addEdge(to, fr, 0)
result = check(graph, 0, n)
print('connected:'+['no','yes'][result[1]])
print('loop:'+['no','yes'][result[0]])




