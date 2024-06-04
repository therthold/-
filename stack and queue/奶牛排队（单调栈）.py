# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:37:14 2024

@author: 86137
"""

N = int(input())
height = [int(input()) for _ in range(N)]

left = [-1] * N
right = [N] * N
stack = []
for idx in range(N):
    while stack and height[stack[-1]] < height[idx]:
        stack.pop()
    if stack:
        left[idx] = stack[-1]
    stack.append(idx)
stack = []
for idx in range(N-1, -1, -1):
    while stack and height[stack[-1]] > height[idx]:
        stack.pop()
    if stack:
        right[idx] = stack[-1]
    stack.append(idx)

result = 0
for i in range(N): ## 遍历每个点的左端点
    for j in range(left[i] + 1, i):  ## 从左端点开始遍历对应点，这个点应当满足右端点＞i
        if right[j] > i:
            result = max(result, i - j + 1)
            break
print(result)
        
        