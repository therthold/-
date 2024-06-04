# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:01:31 2024

@author: 86137
"""

def find(order):
    if order == '':
        return 0
    count = (not order[0] == '.')*2
    result = len(order)-1
    for idx in range(1,len(order)):
        if order[idx] == '.':
            count -= 1
        else:
            count += 1
        if count == 0:
            result = idx
            break
    return result

def change(order):
    if order == '':
        return [], []
    mid_result = []
    pos_result = []
    root = order[0]
    idx = find(order[1:])
    adleft_mid, adleft_pos = change(order[1:idx+1])
    adright_mid, adright_pos = change(order[idx+1:])
    
    mid_result += adleft_mid
    if not root == '.':
        mid_result.append(root)
    mid_result += adright_mid
    
    pos_result += adleft_pos
    pos_result += adright_pos
    if not root == '.':
        pos_result.append(root)
    
    return mid_result, pos_result

order = input()
mid, pos = change(order)
print(''.join(mid))
print(''.join(pos))