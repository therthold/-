# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:49:30 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, root, parent = None, child = None, left = None, right = None):
        self.root = root
        self.parent = parent
        self.child = []
        self.left = left
        self.right = right

def build(order, count):
    trees = [TreeNode(0)]
    target = 0
    height = 0
    result = 0
    for i in order:
        if i == 'd':
            count += 1
            trees.append(TreeNode(count))
            trees[-1].parent = trees[target]
            trees[target].child.append(trees[-1])
            target = trees[-1].root
            height += 1
        elif i == 'u':
            target = trees[target].parent.root
            height -= 1
        result = max(result, height)
    return trees, result

def rebuild(treelist):
    if treelist == []:
        pass
    elif len(treelist) == 1:
        tree = treelist[0]
        tree.left = rebuild(tree.child)
        return tree
    else:
        left = treelist[0]
        right = treelist[1:]
        left.right = rebuild(right)
        left.left = rebuild(left.child)
        return left

def finddepth(tree):
    if tree.left == None and tree.right == None:
        return 0
    elif tree.left == None:
        return 1 + finddepth(tree.right)
    elif tree.right == None:
        return 1 + finddepth(tree.left)
    else:
        return 1 + max(finddepth(tree.right),finddepth(tree.left))
order = input()
trees, height = build(order, 0)
tree = rebuild([trees[0]])
print("%s => %s"%(height, finddepth(tree)))