# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:27:33 2024

@author: 86137
"""
while True:
    try:
        s,t = input().split()
        idx = 0
        flag = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
            if idx == len(s):
                flag = 1
                break
        print(['No','Yes'][flag])
    except EOFError:
        break
    
