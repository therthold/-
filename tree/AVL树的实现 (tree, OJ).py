# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:36:13 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVLtree():
    def __init__(self):
        self.root = None
    
    def leftrotate(self, node):
        newroot = node.right
        newchild = newroot.left
        newroot.left = node
        node.right = newchild
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        newroot.height = 1 + max(self.get_height(newroot.left), self.get_height(newroot.right))
        return newroot
    
    def rightrotate(self, node):
        newroot = node.left
        newchild = newroot.right
        newroot.right = node
        node.left = newchild
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        newroot.height = 1 + max(self.get_height(newroot.left), self.get_height(newroot.right))
        return newroot
    
    def push(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.root = self._push(val, self.root)
    
    def _push(self, val, currentnode):
        if not currentnode:
            return TreeNode(val)
        elif val < currentnode.root:
            currentnode.left = self._push(val, currentnode.left)
        else:
            currentnode.right = self._push(val, currentnode.right)
        currentnode.height = 1 + max(self.get_height(currentnode.left), self.get_height(currentnode.right))
        
        balance = self.get_balance(currentnode)
        if balance > 1:
            if val < currentnode.left.root:
                return self.rightrotate(currentnode)
            else:
                currentnode.left = self.leftrotate(currentnode.left)
                return self.rightrotate(currentnode)

        if balance < -1:
            if val > currentnode.right.root:
                return self.leftrotate(currentnode)
            else:
                currentnode.right = self.rightrotate(currentnode.right)
                return self.leftrotate(currentnode)
        
        return currentnode
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

def preloop(tree, result):
    if not tree == None:
        result.append(str(tree.root))
        result = preloop(tree.left, result)
        result = preloop(tree.right, result)
    return result

n = int(input())
numlist = list(map(int,input().split()))
tree = AVLtree()
for idx in range(n):
    tree.push(numlist[idx])
print(' '.join(preloop(tree.root, [])))

