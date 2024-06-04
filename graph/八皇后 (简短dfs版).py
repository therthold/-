# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:02:44 2024

@author: 86137
"""
def check(i, end_p):
    for j in range(len(end_p)):
        cur = int(end_p[j])
        if abs(cur - i) == abs(len(end_p) - j) or i == cur:
            return False
    else:
        return True

def dfs(n, end_p):
    result = []
    if len(end_p) == n:
        result.append(int(end_p))
    else:
        for i in range(n):
            if check(i, end_p):
                result += dfs(n, end_p + str(i))
    return result

n = 8
result = dfs(n, '')
t = int(input())
for _ in range(t):
    print(result[int(input())-1] + 11111111)