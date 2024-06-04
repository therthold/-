# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:17:04 2024

@author: 86137
"""

def count(num):
    queue = [(1%num, '1')]
    visited = set([1%num])
    
    while queue:
        mod, path = queue.pop(0)
        if mod == 0:
            return path
        for i in ['0','1']:
            new_path = path + i
            new_mod = (mod*10 + int(i))%num
            if new_mod not in visited:
                queue.append((new_mod, new_path))
                visited.add(new_mod)

n = int(input())
while not n == 0:
    print(count(n))
    n = int(input())
