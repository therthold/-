# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:17:46 2024

@author: 86137
"""
import heapq

class Vertex:
    def __init__(self, val):
        self.val = val
        self.connections = {}
    
    def addNeighbor(self, neighbor, weight):
        self.connections[neighbor] = weight

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
        self.ids[fr].addNeighbor(to, weight)

def find(graph, fr, to):
    visited = {fr:0}
    queue = [(0, [fr], fr)]
    heapq.heapify(queue)
    while queue:
        path_length, path, cur = heapq.heappop(queue)
        cur = graph.ids[cur]
        if cur.val == to:
            return path
        for c in cur.connections:
            new_length = cur.connections[c]
            if c not in visited or path_length + new_length < visited[c]:
                visited[c] = path_length + new_length
                heapq.heappush(queue, (path_length + new_length, path + ['->(' + str(new_length) + ')->'+c], c))

Map = Graph()
for _ in range(int(input())):
    key = input()
    Map.addVertex(key)
for _ in range(int(input())):
    fr, to, weight = map(str,input().split())
    Map.addEdge(fr, to, int(weight))
    Map.addEdge(to, fr, int(weight))
for _ in range(int(input())):
    fr, to = map(str,input().split())
    result = find(Map, fr, to)
    print(''.join(result))
    

