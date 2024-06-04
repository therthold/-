# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:22:16 2024

@author: 86137
"""

N = int(input())
while N != 0:
    hotel = []
    result = 0
    for _ in range(N):
        dis, val = map(int,input().split())
        hotel.append([dis, val])
    hotel.sort()
    for i in range(N):
        if i == 0:
            minvalue = hotel[i][1]
            result += 1
        else:
            if hotel[i][1] < minvalue:
                result += 1
                minvalue = hotel[i][1]
    print(result)
    N = int(input())