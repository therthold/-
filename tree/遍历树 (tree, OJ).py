# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:49:51 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, val, child = None, parent = None):
        self.root = val
        self.child = child
        self.parent = parent

def build(trees, position):
    for t in trees:
        if not t.child == None:
            newchild = []
            for c in t.child:
                trees[position[c]].parent = t
                newchild.append(trees[position[c]])
            t.child = newchild
    return trees

def loop(treenode):
    result = []
    if treenode.child == None:
        result.append(str(treenode.root))
    else:
        idx = len(treenode.child)
        for i in range(len(treenode.child)):
            if treenode.child[i].root > treenode.root:
                idx = i
                break
            else:
                result += loop(treenode.child[i])
        result.append(str(treenode.root))
        for rest in treenode.child[idx:]:
            result += loop(rest)
    return result

trees = []
position = {}
n = int(input())
for _ in range(n):
    numlist = list(map(int,input().split()))
    position[numlist[0]] = len(trees)
    trees.append(TreeNode(numlist[0], child = sorted(numlist[1:])))
trees = build(trees, position)
for t in trees:
    if t.parent == None:
        result = loop(t)
        print('\n'.join(result))
        break

    
        
        