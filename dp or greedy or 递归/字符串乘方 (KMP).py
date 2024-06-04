# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:37:06 2024

@author: 86137
"""

def get_next(s):
    result = [0]
    temp = 0
    idx = 1
    while idx < len(s):
        if s[idx] == s[temp]:
            temp += 1
            idx += 1
            result.append(temp)
        elif temp:
            temp = result[temp-1]
        else:
            result.append(0)
            idx += 1
    return result

def count(s):
    s_next = get_next(s)
    cur = len(s)
    idx = 1
    for i in range(1, cur):
        if s_next[i] == s_next[i-1]+1:
            continue
        else:
            idx = i + 1
    return cur//idx if cur%idx == 0 else 1

while True:
    target = input()
    if target == '.':
        break
    print(count(target))