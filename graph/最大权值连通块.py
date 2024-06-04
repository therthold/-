# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:27:59 2024

@author: 86137
"""

class Vertex:
    def __init__(self, key, val):
        self.id = key
        self.necto = {}
        self.val = val
    
    def add(self, nbr, weight = 0):
        self.necto[nbr] = weight
    
    def getConnectTo(self):
        return self.necto.keys()
    
    def getnum(self):
        return len(self.necto)

class Graph:
    def __init__(self):
        self.idlist = {}
        self.num = 0
    
    def addVertex(self, key, key_val):
        self.idlist[key] = Vertex(key, key_val)
        self.num += 1
    
    def addEdge(self, fr, to, fr_val, to_val, weight = 0):
        if fr not in self.idlist:
            self.addVertex(fr, fr_val)
        if to not in self.idlist:
            self.addVertex(to, to_val)
        self.idlist[fr].add(to, weight)

def findmax(Vertex, have, graph):
    res = 0
    if Vertex.id not in have:
        res += Vertex.val
        have.add(Vertex.id)
        connect = Vertex.getConnectTo()
        for c in connect:
            target = graph.idlist[c]
            if target.id not in have:
                res += findmax(target, have, graph)
                have.add(c)
    return res
    
    
n,m = map(int,input().split())
graph = Graph()
value = list(map(int,input().split()))
for i in range(n):
    graph.addVertex(i, value[i]) 
for _ in range(m):
    a,b = map(int,input().split())
    graph.addEdge(a, b, value[a], value[b])
    graph.addEdge(b, a, value[b], value[a])
result = 0
for i in range(n):
    res = findmax(graph.idlist[i], set(), graph)
    result = max(res, result)
print(result)
    