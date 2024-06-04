# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:40:46 2024

@author: 86137
"""

def gpa(score):
    return [4-3*(100-score)**2/1600,0][score < 60]

N, M = map(int,input().split())
result = []
for _ in range(N):
    infor = list(map(int,input().split()))
    code = str(infor[0])
    crd = 0
    total = 0
    while not len(infor) == 1:
        C = infor.pop()
        score = infor.pop()
        crd += C
        total += C*gpa(score)
    result.append([code, total/crd])
result.sort(key = lambda x: x[1], reverse=True)
print(' '.join([result[i][0] for i in range(N)][:M]))