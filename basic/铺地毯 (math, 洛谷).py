# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:40:41 2024

@author: 86137
"""

def check(i, j, carpets):
    result = 0
    for idx in range(len(carpets)-1, -1, -1):
        car_i, car_j, length, width = carpets[idx]
        if i >= car_i and i - car_i <= length and j >= car_j and j - car_j <= width:
            result = idx+1
            break
    return result

n = int(input())
carpets = []
for _ in range(n):
    car_i, car_j, length, width = map(int,input().split())
    carpets.append((car_i, car_j, length, width))
i, j = map(int,input().split())
result = check(i, j, carpets)
print(-1 if result == 0 else result)