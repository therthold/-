# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:18:55 2024

@author: 86137
"""

def humdrum(num):
    stack = []
    result = [0]*len(num)
    for idx in range(len(num)):
        while stack and stack[-1][1] < num[idx]:
            i, _ = stack.pop()
            result[i] = idx + 1
        stack.append((idx, num[idx]))
    return result

def humd(num):
    stack = []
    result = [0]*len(num)
    for idx in range(len(num)):
        while stack and num[stack[-1]] < num[idx]:
            result[stack.pop()] = idx + 1
        stack.append(idx)
    return result

n = int(input())
num = list(map(int, input().split()))
print(*humd(num))

