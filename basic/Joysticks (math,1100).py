# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:33:19 2024

@author: 86137
"""
import math
first, second = map(int,input().split())
result = 0
while first > 0 and second > 0:
    if first <= 2 and second <= 2:
        if first == 2 or second == 2:
            result += 1
        break
    if first >= second:
        second += math.ceil(first/2-1)
        result += math.ceil(first/2-1)
        first = 2 - first%2
    else:
        first += math.ceil(second/2-1)
        result += math.ceil(second/2-1)
        second = 2 - second%2
print(result)