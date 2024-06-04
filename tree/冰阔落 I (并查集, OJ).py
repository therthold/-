# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 06:19:56 2024

@author: 86137
"""

def get_father(x, father):
    if father[x] != x:
        father[x] = get_father(father[x], father)
    return father[x]

def union(x, y, father):
    father_x = get_father(x, father)
    father_y = get_father(y, father)
    if not father_x == father_y:
        father[father_y] = father_x


while True:
    try:
        n,m = map(int,input().split())
        code = [i for i in range(n+1)]
        for _ in range(m):
            x,y = map(int,input().split())
            if get_father(x, code) == get_father(y, code):
                print('Yes')
            else:
                print('No')
                union(x, y, code)
        coke = set(get_father(i, code) for i in range(1,n+1))
        result = sorted(coke)
        print(len(result))
        print(*result)
    
    except EOFError:
        break

        