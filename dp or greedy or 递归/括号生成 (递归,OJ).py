# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:44:52 2024

@author: 86137
"""

N = int(input())
def write(num, result, left = 0, right = 0, s = ''):
    if len(s) == num*2:
        result.append(s)
    else:
        if left < num:
            write(num, result, left+1, right, s+'(')
        if right < num and right < left:
            write(num, result, left, right+1, s+')')
    return result
result = write(N, [])
result.sort()
for i in result:
    print(i)
