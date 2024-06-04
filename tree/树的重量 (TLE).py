# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:52:07 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None
        self.val = 0
        self.childval = 0


def increase(treenode, trees, value):
    idx = treenode.root
    pre = treenode.childval
    treenode.val += value
    child = 0
    if idx*2 - 1 < len(trees):
        increase(trees[idx*2-1], trees, value)
        child = 1
    if idx*2 < len(trees):
        increase(trees[idx*2], trees, value)
        child = 2
    
    if child == 2:
        treenode.childval = trees[idx*2-1].childval + trees[idx*2].childval + treenode.val
    elif child == 1:
        treenode.childval = trees[idx*2-1].childval + treenode.val
    else:
        treenode.childval += value
    inc = treenode.childval - pre
    return trees, inc

def update(treenode, trees, value):
    idx = treenode.root
    while idx//2 > 0:
        trees[idx//2 - 1].childval += value
        idx = idx//2

k,n = map(int,input().split())
trees = [TreeNode(i) for i in range(1, 2**k)]
for _ in range(n):
    order = input().split()
    if order[0] == '1':
        idx = int(order[1])-1
        value = int(order[2])
        trees, inc = increase(trees[idx], trees, value)
        update(trees[idx], trees, inc)
    elif order[0] == '2':
        idx = int(order[1])-1
        print(trees[idx].childval)

