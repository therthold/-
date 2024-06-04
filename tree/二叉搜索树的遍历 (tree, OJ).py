# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 19:40:00 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, key, left = None, right = None, parent = None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        
def rebuild(keylist):
    if len(keylist) == 1:
        return TreeNode(keylist[0])
    root = keylist[0]
    idx = 1
    for i in range(1, len(keylist)):
        if keylist[i] > root:
            idx = i
            break
    temp = TreeNode(root)
    if not len(keylist[1:idx]) == 0:
        temp.left = rebuild(keylist[1:idx])
    if not len(keylist[idx:]) == 0:
        temp.right = rebuild(keylist[idx:])
    return temp

def postloop(tree, result):
    if not tree == None:
        result = postloop(tree.left, result)
        result = postloop(tree.right, result)
        result.append(str(tree.key))
    return result


n = int(input())
numlist = list(map(int,input().split()))
tree = rebuild(numlist)
result = []
print(' '.join(postloop(tree, result)))
