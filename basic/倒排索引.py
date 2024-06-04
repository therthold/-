# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:31:52 2024

@author: 86137
"""

N = int(input())
files = {}
for i in range(N):
    words = list(map(str,input().split()))[1:]
    for word in words:
        if word not in files:
            files[word] = [str(i+1)]
        else:
            if str(i+1) not in files[word]:
                files[word].append(str(i+1))
M = int(input())
for _ in range(M):
    word = input()
    print(' '.join(files[word])if word in files else 'NOT FOUND')