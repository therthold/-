# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:16:30 2024

@author: 86137
"""

def check(codes):
    root = codes[0]
    if root == '#':
        return 'F'
    idx = 1
    cur = 2
    while idx < len(codes) and cur > 0:
        if codes[idx] == '#':
            cur -= 1
        else:
            cur += 1
        idx += 1
    if cur == 0 and idx == len(codes):
        return 'T'
    return 'F'

while True:
    N = int(input())
    if N == 0: break
    codes = input().split()
    print(check(codes))
    