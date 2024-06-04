# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:05:39 2024

@author: 86137
"""

def DevideBy2(number):
    H = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    remain = []
    while number != 0:
        remain.append(H[number%2])
        number = number // 2
    result = ''
    flag = 0
    for i in range(len(remain)-1,-1,-1):
        if remain[i] == '1' and not flag:
            if i == 0:
                result += '2(0)'
            elif i == 1:
                result += '2'
            elif i == 2:
                result += '2(2)'
            else:
                result += '2(' + DevideBy2(i) + ')'
            flag = 1
        elif remain[i] == '1' and flag:
            if i == 0:
                result += '+2(0)'
            elif i == 1:
                result += '+2'
            elif i == 2:
                result += '+2(2)'
            else:
                result += '+2(' + DevideBy2(i) + ')'
    return result
print(DevideBy2(int(input())))