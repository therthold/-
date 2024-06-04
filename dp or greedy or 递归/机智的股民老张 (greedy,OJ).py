# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:53:32 2024

@author: 86137
"""

values = list(map(int,input().split()))
result = 0
if values[1] > values[0]:
    result = values[1] - values[0]
    start = values[0]
else:
    start = values[1]
for i in range(2,len(values)):
    if values[i] >= start:
        result = max(result, values[i] - start)
    else:
        start = values[i]
print(result)