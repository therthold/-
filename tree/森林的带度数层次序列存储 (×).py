# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:52:21 2024

@author: 86137
"""
# C 3 E 3 F 2 G 1 K 0 H 0 J 1 U 0 P 2 Y 0 Q 0 A 0 B 0
# K H Q J E U A B P F Y G C

def loop(templist, widthlist, start, end, count):
    if end > len(templist):
        return []
    result = []
    jump = sum(widthlist[start:end])
    add = 0
    for idx in range(start, end):
        count -= 1
        temp = templist[idx]
        width = widthlist[idx]
        if not width == 0:
            result += loop(templist, widthlist, end + add, end + jump, width)
            add += width
        result.append(temp)
        if count == 0:
            break
    return result


n = int(input())
result = []
for _ in range(n):
    trees = input().split(' ')
    temps = trees[::2]
    widths = list(map(int,trees[1::2]))
    result += loop(temps, widths, 0, 1, widths[0])
print(' '.join(result))