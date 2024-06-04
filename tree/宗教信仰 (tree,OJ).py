# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:40:47 2024

@author: 86137
"""
class TreeNode(object):
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
    
def findroot(treenode):
    if treenode.parent == None:
        return treenode.key
    else:
        return findroot(treenode.parent)

n,m = map(int,input().split())
count = 0
while not n == 0 and not m == 0:
    count += 1
    trees = [TreeNode(i) for i in range(n)]
    result = 0
    for _ in range(m):
        i,j = map(int,input().split())
        i,j = findroot(trees[i-1]), findroot(trees[j-1])
        if j < i:
            trees[i].parent = trees[j]
        elif j > i:
            trees[j].parent = trees[i]
    for i in range(n):
        if trees[i].parent == None:
            result += 1
    print('Case %s: %s'%(count, result))
    n,m = map(int,input().split())
    
    
    