# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:28:10 2024

@author: 86137
"""

class TreeNode(object):
    def __init__(self, root, left = None, right = None, parent = None, depth = 0):
        self.root = root
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = depth

def trans_to_trees(mid, post):
    if len(mid) == 1 or len(post) == 1:
        return TreeNode(mid)
    elif len(mid) > 1 or len(post) > 1:
        root = post[-1]
        idx = mid.find(root)
        temp = TreeNode(root)
        if not trans_to_trees(mid[:idx], post[:idx]) == None:
            temp.left = trans_to_trees(mid[:idx], post[:idx])
        if not trans_to_trees(mid[idx+1:], post[idx:-1]) == None:
            temp.right = trans_to_trees(mid[idx+1:], post[idx:-1])
        return temp

n = int(input())
for _ in range(n):
    mid = input()
    post = input()
    tree = trans_to_trees(mid, post)
    result = []
    queue = [tree]
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.root)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result += current_level
    print(''.join(result))
    




