# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:00:23 2024

@author: 86137
"""
def change(s):
    if len(s) == 1:
        return '0' + s + '.'
    else:
        return s + '.'

N = int(input())
code = []
for _ in range(N):
    code.append(input())
code.sort(key = lambda x: ''.join(map(change,x.split('.')))[:-1])
for c in code:
    print(c)
