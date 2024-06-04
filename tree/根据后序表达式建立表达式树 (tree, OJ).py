# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:28:43 2024

@author: 86137
"""


class TreeNode(object):
    def __init__(self, root, left = None, right = None, parent = None):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent

def trans_to_tree(formula):
    if formula:
        key = formula.pop()
        if key.islower():
            temp = TreeNode(key)
        elif key.isupper():
            temp = TreeNode(key)
            temp.left = trans_to_tree(formula)
            temp.right = trans_to_tree(formula)
    return temp
    
def layerloop(treenode, result = []):
    queue = [treenode]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            result.append(node.root)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
    return ''.join(result)

n = int(input())
for i in range(n):
    formula = list(input())
    result = []
    print(layerloop(trans_to_tree(formula), result)[::-1])
    