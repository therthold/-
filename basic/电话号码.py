# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:24:38 2024

@author: 86137
"""

t = int(input())
for _ in range(t):
    n = int(input())
    code = set()
    telephone = []
    for i in range(n):
        number = input()
        telephone.append([number, len(number)])
    telephone.sort(key = lambda x:x[1], reverse=True)
    maxl = telephone[0][1]
    minl = telephone[-1][1]
    length = {i:set() for i in range(minl, maxl+1)}
    check = False
    for number in telephone:
        number = number[0]
        l = len(number)
        if number in length[l]:
            check = True
            break
        else:
            for i in range(minl, l+1):
                length[i].add(number[:i])
    if check:
        print('NO')
    else:
        print('YES')
        