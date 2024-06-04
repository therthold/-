# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:08:44 2024

@author: 86137
"""

while True:
    try:
        target = input()
        L = list(map(str,target.split()))
        I = int(L[0])
        T = ''.join(L[1:])[1:].split('(')
        result = {'(':target.count('('), ')':0}
        idx = 0
        num = []
        S = 0
        while not result['(']+(idx==0) == result[')']:
            if idx >= len(T):
                target = input()
                result['('] += target.count('(')
                newT = list(map(str,target.split()))
                T += ''.join(newT).split('(')
            if T[idx] == '':
                del T[idx]
                idx -=1
            else:
                if not ')' in T[idx]:
                    S += int(T[idx])
                    num.append(int(T[idx]))
                elif ')' in T[idx] and ')' in T[idx-1]:
                    result[')'] += 1
                    if T[idx-1] == ')':
                        result[S] = S
                    for _ in range(len(T[idx])-1):
                        S -= num.pop()
                        result[')'] += 1
                elif ')' in T[idx]:
                    result[')'] += len(T[idx])
            idx += 1
        print(['no','yes'][I in result])
    except EOFError:
        break