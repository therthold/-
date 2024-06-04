# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:15:39 2024

@author: 86137
"""

queue = []
N,M = map(int,input().split())
words = input().split()
result = 0
for word in words:
    if word not in queue:
        if len(queue) == N:
            queue.pop(0)
            queue.append(word)
        else:
            queue.append(word)
        result += 1
print(result)