# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:39:39 2024

@author: 86137
"""

def change(time):
    hour, minute, second = map(int,time.split(':'))
    return 3600*hour + 60*minute + second

n = int(input())
web = {}
for _ in range(n):
    w, start, end = map(str,input().split())
    time = change(end) - change(start)
    if w in web:
        web[w] += time
    else:
        web[w] = time
result = sorted(web, key = lambda x: web[x])
print(result[-1])