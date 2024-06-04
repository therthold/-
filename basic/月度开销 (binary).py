# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:08:12 2024

@author: 86137
"""

def check(x, values, limit):
    num, total = 1, 0
    idx = 0
    while idx < len(values) and num <= limit:
        if total + values[idx] > x:
            total = values[idx]
            num += 1
        else:
            total += values[idx]
        idx += 1
    return num <= limit

def binary(values, limit):
    result = 1
    left, right = max(values), sum(values)
    while left < right:
        mid = (left + right)//2
        if check(mid, values, limit): # 说明mid值偏大，可以涵盖
            result = mid
            right = mid
        else:
            left = mid + 1 # 说明mid值偏小，可以涵盖
    return result

N, M = map(int, input().split())
values = []
for _ in range(N):
    values.append(int(input()))
print(binary(values, M))