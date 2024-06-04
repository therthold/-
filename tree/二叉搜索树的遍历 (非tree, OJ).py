# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:50:36 2024

@author: 86137
"""

def findidx(treelist):
    key = treelist[0]
    idx = 0
    for i in range(1,len(treelist)):
        if treelist[i] > key:
            idx = i
            break
    return idx

def rebuild(treelist, result):
    if len(treelist) == 0:
        pass
    elif len(treelist) <= 1:
        result.append(str(treelist[0]))
    else:
        idx = findidx(treelist)
        if idx == 0:
            result += rebuild(treelist[1:], [])
        else:
            result += rebuild(treelist[1:idx], []) + rebuild(treelist[idx:], [])
        result.append(str(treelist[0]))
    return result

n = int(input())
treelist = list(map(int,input().split()))
print(' '.join(rebuild(treelist, [])))