# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:34:51 2024

@author: 86137
"""


queue = []
group = {}
have = {}
t = int(input())
for i in range(t):
    people = input().split()
    for p in people:
        group[p] = i
order = list(map(str,input().split()))
while not order[0] == 'STOP':
    command = order[0]
    if command == 'ENQUEUE':
        person = order[1]
        if person in group:
            code = group[person]
        else:
            code = i+1
            i += 1
            group[person] = code
        if code in have:
            for i in have:
                if have[i][0] >= have[code][0]:
                    have[i][0] += 1
            have[code][1] += 1
            queue.insert(have[code][0], person)
        else:
            have[code] = [len(queue),1]
            queue.append(person)
    elif command == 'DEQUEUE':
        result = queue.pop(0)
        code = group[result]
        for i in have:
            have[i][0] -= 1
        have[code][1] -= 1
        if have[code][1] == 0:
            del have[code]
        print(result)
    order = list(map(str,input().split()))  