# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 07:39:02 2024

@author: 86137
"""


class TreeNode(object):
    def __init__(self, key, left = None, right = None, parent = None, depth = 1):
        self.root = key
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = depth
    
    def isleaf(self):
        return self.left == None and self.right == None

def finddepth(treenode, trees):
    if treenode.isleaf():
        treenode.depth = 1
    if not treenode.left == None:
        finddepth(treenode.left, trees)
        treenode.depth = max(treenode.left.depth + 1, treenode.depth)
    if not treenode.right == None:
        finddepth(treenode.right, trees)
        treenode.depth = max(treenode.right.depth + 1, treenode.depth)
    return treenode.depth

def findroot(trees):
    for tree in trees:
        if tree.parent == None:
            return tree.root

n = int(input())
trees = [TreeNode(i) for i in range(n)]
numleaf = 0
for i in range(n):
    left, right = map(int,input().split())
    if not left == -1:
        trees[i].left = trees[left]
        trees[left].parent = trees[i]   
    if not right == -1:
        trees[i].right = trees[right]
        trees[right].parent = trees[i]
    if left == -1 and right == -1:
        numleaf += 1
root = findroot(trees)
depth = finddepth(trees[root], trees)
print("%s %s"%(depth-1, numleaf))
