# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:10:44 2024

@author: 86137
"""

n,k = map(int,input().split())
Max = 100000
if n >= k:
    print(n-k)
else:
    queue = [[n,0]]
    visit = [0]*(Max+1)
    while not queue == []:
        position = queue.pop(0)
        if position[0] == k:
            print(position[1])
            break
        else:
            p = position[0]
            step = position[1]
            if p - 1 >= 0 and visit[p - 1] == 0:
                queue.append([p - 1,step + 1])
                visit[p-1] = 1
            if p + 1 <= Max and visit[p + 1] == 0:
                queue.append([p + 1, step + 1])
                visit[p+1] = 1
            if p * 2 <= Max and visit[p * 2] == 0:
                queue.append([p * 2, step + 1])
                visit[p*2] = 1