# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:33:44 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, val, parent = None):
        self.root = val
        self.left = None
        self.right = None
        self.parent = parent
    
    def addchild(self, newchild):
        if self.left == None:
            self.left = newchild
        elif self.right == None:
            self.right = newchild

def build(temps):
    if temps == []:
        return None
    elif len(temps) == 1:
        return TreeNode(temps[0][0])
    else:
        root = TreeNode(temps[0][0])
        while len(temps) >= 2:
            temp = temps[1]
            newchild = TreeNode(temp[0], parent = root)
            if temp[1] == '1':
                root.addchild(newchild)
                while not root.right == None and not root.parent == None:
                    root = root.parent
            else:
                root.addchild(newchild)
                if not root.right == None:
                    root = root.right
                else:
                    root = root.left
            temps = temps[1:]
        return root

def getright(treenode):
    trees = []
    if not treenode.root[0] == '$':
        trees.append(treenode)
        if not treenode.right == None:
            addtr = getright(treenode.right)
            trees += addtr
    return trees

def loop(trees):
    result = []
    addtree = []
    if len(trees) == 0:
        return result
    else:
        for idx in range(len(trees)):
            temp = trees[idx]
            result.append(temp.root)
            if not temp.left == None:
                readd = getright(temp.left)
                addtree += readd
        result.reverse()
        result += loop(addtree)
        return result

N = int(input())
temps = input().split()
tree = build(temps)
result = loop([tree])
print(' '.join(result))
            