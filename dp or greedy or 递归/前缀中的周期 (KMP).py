# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:44:50 2024

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

def pre(s, ID):
    print('Test case #%d'%(ID))
    s_next = get_next(s)
    cur_l = 1
    for idx in range(1, len(s)):
        if s_next[idx] == s_next[idx-1] + 1:
            if (idx + 1)%cur_l == 0:
                print('%d %d'%(idx+1, (idx + 1)//cur_l))
        else:
            cur_l = idx + 1 - s_next[idx] # 更新长度，减数项对应着idx位置之前的重复序列

ID = 0
while True:
    ID += 1
    l = int(input())
    if l == 0:
        break
    target = input()
    pre(target, ID)
    print('')