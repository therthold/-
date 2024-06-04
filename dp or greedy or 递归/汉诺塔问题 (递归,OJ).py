# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:25:13 2024

@author: 86137
"""

num, A, B, C = input().split()
position = [A, B, C]
num = int(num)
def move(num, fr, to):
    if num == 1:
        print("%s:%s->%s"%(num, position[fr], position[to]))
    else:
        move(num-1, fr, 3-fr-to)
        print("%s:%s->%s"%(num, position[fr], position[to]))
        move(num-1, 3-fr-to, to)
move(num, 0, 2)