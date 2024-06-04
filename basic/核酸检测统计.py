# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:48:07 2024

@author: 86137
"""

n = int(input())
m = int(input())
infor = {}
date = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
stu = {}
for _ in range(n):
    student, fac = map(str,input().split())
    stu[student] = fac
    if fac not in infor:
        infor[fac] = [0,0]
    infor[fac][1] += 1
for _ in range(m):
    day, student = map(str,input().split())
    date[day].append(student)
result = []
for student in stu:
    if student not in date['1']:
        result.append(student)
        infor[stu[student]][0] += 1
    else:
        rest = 3
        for i in range(9):
            if student not in date[str(i+1)]:
                rest -= 1
            else:
                rest = 3
            if rest == 0:
                result.append(student)
                infor[stu[student]][0] += 1
                break
print(len(result))
print(max(infor, key=lambda x: infor[x][0]/infor[x][1]))