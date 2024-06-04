# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 09:28:16 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, key, dirs = [], files = [], layer = 0, pre = None):
        self.key = key
        self.dirs = dirs
        self.files = files
        self.layer = layer
        self.pre = pre

def write(treenode):
    print('|     '*treenode.layer + treenode.key)
    for dr in treenode.dirs:
        write(dr)
    treenode.files.sort()
    for fl in treenode.files:
        print('|     '*treenode.layer + fl)
    

code = 0
word = 'ROOT'
Node = TreeNode(word)
while not word == '#':
    if word == '*':
        code += 1
        print('DATA SET %s:'%code)
        write(Node)
        print()
        Node = TreeNode('ROOT', dirs = [], files = [], layer = 0)
    elif word[0] == 'f':
        Node.files.append(word)
    elif word[0] == 'd':
        newNode = TreeNode(word, dirs = [], files = [], layer = 0)
        Node.dirs.append(newNode)
        newNode.pre = Node
        newNode.layer = Node.layer + 1
        Node = newNode
    elif word == ']':
        Node = Node.pre
    word = input()
        
        
        