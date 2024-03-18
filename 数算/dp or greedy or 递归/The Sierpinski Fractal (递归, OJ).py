# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:12:08 2024

@author: 86137
"""

def write(num):
    result = []
    if num == 1:
        result.append(' /\\')
        result.append('/__\\')
    else:
        result = write(num-1)
        l = len(result)
        for idx in range(l):
            result.append(result[idx] + ' '*(l-idx-1) + result[idx])
            result[idx] = ' '*2**(num-1) + result[idx]
    return result

n = int(input())
while not n == 0:
    print('\n'.join(write(n)))
    print('')
    n = int(input())
    