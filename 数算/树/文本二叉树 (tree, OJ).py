# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:43:59 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, root, left = None, right = None, parent = None, depth = 0):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = depth

def preloop(tree, result):
    if (not tree == None) and (not tree.root == '*') and (not tree.root == ''):
        result.append(str(tree.root))
        result = preloop(tree.left, result)
        result = preloop(tree.right, result)
    return result

def midloop(tree, result):
    if (not tree == None) and (not tree.root == '*') and (not tree.root == ''):
        result = midloop(tree.left, result)
        result.append(str(tree.root))
        result = midloop(tree.right, result)
    return result

def postloop(tree, result):
    if (not tree == None) and (not tree.root == '*') and (not tree.root == ''):
        result = postloop(tree.left, result)
        result = postloop(tree.right, result)
        result.append(str(tree.root))
    return result

n = int(input())
for _ in range(n):
    trees = []
    key = input()
    while not key == '0':
        depth = len(key[:-1])
        temp = TreeNode(key[-1], depth = depth)
        for i in range(len(trees)-1,-1,-1):
            if trees[i].depth == depth - 1:
                temp.parent = trees[i]
                if i == len(trees)-1:
                    trees[i].left = temp
                else:
                    trees[i].right = temp
                break
        trees.append(temp)
        key = input()
    result = []
    print(''.join(preloop(trees[0], result)))
    result = []
    print(''.join(postloop(trees[0], result)))
    result = []
    print(''.join(midloop(trees[0], result))+'\n')
    
        
        