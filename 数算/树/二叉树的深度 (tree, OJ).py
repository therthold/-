# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 10:24:54 2024

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
n = int(input())
trees = [TreeNode(1) for i in range(n)]
for i in range(n):
    left, right = map(int,input().split())
    if not left == -1:
        trees[i].left = trees[left-1]
        trees[left-1].parent = trees[i]   
    if not right == -1:
        trees[i].right = trees[right-1]
        trees[right-1].parent = trees[i]
print(finddepth(trees[0], trees))
        
