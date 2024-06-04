# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:26:36 2024

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
            ## 本质上是依据已选出的串B确定重新开始的串A长度，其中串B终于s[idx-1]，串A始于s[0]
            temp = result[temp-1] # 这里为temp-1是因为result存储的是长度，因此更新后对于s[temp]也就是新的重复串的后一位字符
        else:
            result.append(0)
            idx += 1
    return result
        
def match(target, origin):
    target_next = get_next(target)
    idx = 0
    temp = 0
    while idx < len(origin):
        if target[temp] == origin[idx]:
            temp += 1
            idx += 1
        elif temp:
            temp = target_next[temp-1]
        else:
            idx += 1
#        print(temp)
#        print(idx)
        if temp == len(target):
            return idx - temp
    return -1


while True:
    origin = input()
    target = input()
    print(match(target, origin))
    