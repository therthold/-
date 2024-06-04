# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 00:44:20 2024

@author: 86137
"""

n = int(input())
for i in range(n):
    left = 0
    right = 0
    a,b = map(int,input().split())
    while not a == 1 or not b == 1:
        if a < b:
            right += (b-1)//a
            a,b = a,(b-1)%a+1
        elif a >= b:
            left += (a-1)//b
            a,b = (a-1)%b+1,b
    print('Scenario #%s:'%(i+1))
    print(left,right)
    print('')
    