# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 11:12:02 2024

@author: 86137
"""

n = int(input())
num = list(map(int,input().split()))
result = 0
while len(num) > 1:
    num.sort()
    num[1] = num[0] + num[1]
    result += num[1]
    num = num[1:]
print(result)