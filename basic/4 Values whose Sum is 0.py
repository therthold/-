# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:03:29 2024

@author: 86137
"""

def add(A, a, num):
    if a in A:
        A[a] += num
    else:
        A[a] = num

n = int(input())
result = 0
A = {}
B = {}
C = {}
D = {}
for _ in range(n):
    a,b,c,d = map(int,input().split())
    add(A,a,1)
    add(B,b,1)
    add(C,-c,1)
    add(D,-d,1)
sumAB = {}
for a in A:
    for b in B:
        add(sumAB, a+b, A[a]*B[b])
for c in C:
    for d in D:
        if c+d in sumAB:
            result += sumAB[c+d]*C[c]*D[d]
print(result)