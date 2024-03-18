# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:01:45 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, root, child = []):
        self.root = root
        self.child = child

def preloop(tree, result):
    if not tree == None:
        result.append(str(tree.root))
        for child in tree.child:
            result = preloop(child, result)
    return result

def postloop(tree, result):
    if not tree == None:
        for child in tree.child:
            result = postloop(child, result)
        result.append(str(tree.root))
    return result

def rebuild(treestr):
    if len(treestr) == 1:
        return TreeNode(treestr)
    elif len(treestr) > 1:
        temp = TreeNode(treestr[0], child = [])
        children = treestr[2:-1].split(',')
        child = ''
        for i in children:
            child += i
            if len(child) == 1:
                temp.child.append(rebuild(child))
                child = ''
            elif not child.count('(') == child.count(')'):
                child += ','
            else:
                temp.child.append(rebuild(child))
                child = '' 
        return temp
s = input()
tree = rebuild(s)
result = []
print(''.join(preloop(tree, result)))
result = []
print(''.join(postloop(tree, result)))