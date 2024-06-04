# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:38:12 2024

@author: 86137
"""

class Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, words):
        curr = self.root
        for word in words:
            if word not in curr.children:
                curr.children[word] = Node()
            curr = curr.children[word]
    
def dfs(file, layer = 0):
    result = []
    root = sorted(file.children)
    for path in root:
        result.append(' '*layer + path)
        result += dfs(file.children[path], layer + 1)
    return result

n = int(input())
files = Trie()
for _ in range(n):
    path = list(map(str,input().split('\\')))
    files.insert(path)
print('\n'.join(dfs(files.root)))

# WINNT\SYSTEM32\CERTSRV\CERTCO~1\X86