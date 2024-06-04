# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 08:55:16 2024

@author: 86137
"""

n = int(input())
q1 = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
code = ['A','B','C','D']
puke = input().split()
for p in puke:
    q1[p[1]].append(p)
req = []
for key in q1:
    req += q1[key]
    print('Queue%s:'%key + ' '.join(q1[key]))
q1 = {'A':[],'B':[],'C':[],'D':[]}
for p in req:
    q1[p[0]].append(p)
req = []
for key in q1:
    req += q1[key]
    print('Queue%s:'%key + ' '.join(q1[key]))
print(' '.join(req))
    
