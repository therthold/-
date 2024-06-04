# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:29:04 2024

@author: 86137
"""

def change(s):
    if len(s) == 1:
        if s == '1':
            return 'I'
        elif s == '0':
            return 'B'
    else:
        if '0' in s and '1' in s:
            root = 'F'
        else:
            root = ['B','I']['1' in s]
        idx = len(s)//2
        return change(s[:idx]) + change(s[idx:]) + root

N = int(input())
S = input()
print(change(S))