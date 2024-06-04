# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:57:51 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, root, left = None, right = None, parent = None):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent

def trans_to_trees(pre = None, mid = None, post = None):
    if post == None:
        if len(pre) <= 1 or len(mid) <= 1:
            return TreeNode(pre)
        else:
            root = pre[0]
            idx = mid.find(root)
            temp = TreeNode(root)
            temp.left = trans_to_trees(pre[1:1+idx], mid[:idx], post)
            temp.right = trans_to_trees(pre[1+idx:], mid[idx+1:], post)
            return temp
    
    elif mid == None:
        error = 'mid is necessary'
        return error
    
    elif pre == None:
        if len(mid) <= 1 or len(post) <= 1:
            return TreeNode(mid)
        else:
            root = post[-1]
            idx = mid.find(root)
            temp = TreeNode(root)
            temp.left = trans_to_trees(pre, mid[:idx], post[:idx])
            temp.right = trans_to_trees(pre, mid[idx+1:], post[idx:-1])
            return temp
        
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

mid = input()
post = input()
tree = trans_to_trees(None, mid, post)
result = []
print(''.join(preloop(tree, result)))


