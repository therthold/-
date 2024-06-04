# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:09:51 2024

@author: 86137
"""

def bfs(start, end, buckets):
    queue = [(start,[start])]
    visited = set(start)
    while queue:
        word, path = queue.pop(0)
        if word == end:
            return ' '.join(path)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            for nbr in buckets[bucket]:
                if nbr not in visited:
                    queue.append((nbr, path + [nbr]))
                    visited.add(nbr)
    return 'NO'

from collections import defaultdict
buckets = defaultdict(list)
n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)
    for i in range(len(word)):
        bucket = word[:i] + '_' + word[i+1:]
        buckets[bucket].append(word)
start, end = input().split()
print(bfs(start, end, buckets))