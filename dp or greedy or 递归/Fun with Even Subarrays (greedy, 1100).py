# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:40:22 2024

@author: 86137
"""

t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int,input().split()))
    target = num[-1]
    idx = n-1
    count = 1
    result = 0
    while idx > 0:
        if num[idx-1] == target:
            count += 1
            idx -= 1
        elif idx < count:
            result += (not num[:idx] == [target]*idx)
            idx -= count
        elif not num[idx-count:idx] == [target]*count:
            result += 1
            idx -= count
            count = count*2
    print(result)
            