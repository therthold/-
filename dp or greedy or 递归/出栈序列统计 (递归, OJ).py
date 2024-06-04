# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:49:05 2024

@author: 86137
"""

n = int(input())
stack = []
left = [0]*n
out = []
result = 0
def count(stack, left, out, n, result):
    if len(out) == n:
        result = 1
    else:
        if left:
            stack.append(left.pop())
            result += count(stack, left, out, n, 0)
            left.append(stack.pop())
        if stack:
            out.append(stack.pop())
            result += count(stack, left, out, n, 0)
            stack.append(out.pop())
    return result
print(count(stack, left, out, n, result))
