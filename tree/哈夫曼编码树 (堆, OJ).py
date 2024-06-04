# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:20:59 2024

@author: 86137
"""
import heapq

class TreeNode(object):
    def __init__(self, val_list, weight, left = None, right = None):
        self.val = val_list
        self.weight = weight
        self.left = left
        self.right = right
        self.code = []
    
    def isleaf(self):
        return self.left == None and self.right == None

n = int(input())
codes = []
for _ in range(n):
    code = input().split()
    code, weight = code[0], int(code[1])
    temp = TreeNode([code], weight)
    codes.append([weight, ord(code), temp])
heapq.heapify(codes)
for i in range(n-1):
    left = heapq.heappop(codes)
    right = heapq.heappop(codes)
    neword = min(left[1], right[1])
    newweight = left[0]+right[0]
    newtemp = TreeNode(left[2].val+right[2].val, newweight)
    if left[2].code == []:
        newtemp.code.append('0')
    else:
        for idx in left[2].code:
            newtemp.code.append('0'+idx)
    if right[2].code == []:
        newtemp.code.append('1')
    else:
        for idx in right[2].code:
            newtemp.code.append('1'+idx)
    newtemp.left = left[2]
    newtemp.right = right[2]
    heapq.heappush(codes, [newweight, neword, newtemp])
tree = codes[0][2]
codes = {}
recodes = {}
for i in range(n):
    codes[tree.val[i]] = tree.code[i]
    recodes[tree.code[i]] = tree.val[i]

while True:
    try:
        order = input()
        result = ''
        o = ''
        if '0' in order or '1' in order:
            for idx in range(len(order)):
                o += order[idx]
                if o in recodes:
                    result += recodes[o]
                    o = ''
        else:
            for idx in range(len(order)):
                o += order[idx]
                if o in codes:
                    result += codes[o]
                    o = ''
        print(result)
    except EOFError:
        break

    