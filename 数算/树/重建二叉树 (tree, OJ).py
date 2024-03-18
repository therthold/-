# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:45:31 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, root, left = None, right = None, parent = None):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent

def trans_to_post(pre, mid, trees = []):
    if len(pre) <= 1 and len(mid) <= 1:
        trees = [TreeNode(pre)] + trees
        return trees
    else:
        root = pre[0]
        idx = mid.find(root)
        temp = TreeNode(root)
        temp.left = trans_to_post(pre[1:1+idx], mid[:idx], trees)[0]
        temp.right = trans_to_post(pre[1+idx:], mid[idx+1:], trees)[0]
        trees = [temp] + trees
        return trees

def postloop(tree, result):
    if (not tree == None) and (not tree.root == '*') and (not tree.root == ''):
        result = postloop(tree.left, result)
        result = postloop(tree.right, result)
        result.append(str(tree.root))
    return result

while True:
    try:
        pre, mid = map(str,input().split())
        trees = trans_to_post(pre, mid)
        result = []
        print(''.join(postloop(trees[0], result)))
    except EOFError:
        break

        