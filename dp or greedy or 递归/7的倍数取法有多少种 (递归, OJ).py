# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:06:18 2024

@author: 86137
"""

def divedeBy7(numlist, idx, Sum, mod):
    if idx == len(numlist):
        if mod == 0:
            return 1
        return 0
    else:
        count = divedeBy7(numlist, idx+1, Sum+numlist[idx], (mod+numlist[idx])%7)
        count += divedeBy7(numlist, idx+1, Sum, mod)
    return count


t = int(input())
for _ in range(t):
    numlist = list(map(int,input().split()))[1:]
    print(divedeBy7(numlist, 0, 0, 0))
    