# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:37:53 2024

@author: 86137
"""

ori = list(input())
stack = []
num = set('0123456789')
for idx in range(len(ori)):
    if ori[idx] == ']':
        cur = ''
        idx = 0
        while not stack[-1] == '[':
            if stack[-1] in num:
                idx += 1
            cur = stack.pop() + cur
        stack.pop()
        cur = int(cur[:idx]) * cur[idx:]
        stack.append(cur)
    else:
        stack.append(ori[idx])
print(''.join(stack))
