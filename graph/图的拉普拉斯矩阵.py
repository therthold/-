# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:48:07 2024

@author: 86137
"""

class Vertex:
    def __init__(self, key):
        self.id = key
        self.necto = {}
    
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
    
    def addVertex(self, key):
        self.idlist[key] = Vertex(key)
        self.num += 1
    
    def addEdge(self, fr, to, weight = 0):
        if fr not in self.idlist:
            self.addVertex(fr)
        if to not in self.idlist:
            self.addVertex(to)
        self.idlist[fr].add(to, weight)

n,m = map(int,input().split())
graph = Graph()
for _ in range(m):
    a,b = map(int,input().split())
    graph.addEdge(a, b)
    graph.addEdge(b, a)
for i in range(n):
    result = ['0']*n
    if i in graph.idlist:
        target = graph.idlist[i]
        result[i] = str(target.getnum())
        connected = target.getConnectTo()
        for c in connected:
            result[c] = '-1'
    print(' '.join(result))
    
    
    
    
    