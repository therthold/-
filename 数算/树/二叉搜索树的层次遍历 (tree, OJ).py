# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:13:37 2024

@author: 86137
"""
class TreeNode(object):
    def __init__(self, root, left = None, right = None, parent = None):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent

def layerloop(treenode, result = []):
    queue = [treenode]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            result.append(str(node.root))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ' '.join(result)

numlist = list(map(int,input().split()))
n = len(numlist)
trees = [TreeNode(i) for i in range(n)]
for i in range(n):
    trees[i].root = numlist[i]
    temp = trees[0]
    while temp:
        if temp.root == numlist[i]:
            break
        elif temp.root < numlist[i] and not temp.right == None:
            temp = temp.right
        elif temp.root > numlist[i] and not temp.left == None:
            temp = temp.left
        elif temp.root < numlist[i]:
            temp.right = trees[i]
            break
        elif temp.root > numlist[i]:
            temp.left = trees[i]
            break
print(layerloop(trees[0]))
        