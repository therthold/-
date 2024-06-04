# -*- coding: utf-8 -*-
"""
Created on Mon May 20 19:21:27 2024

@author: 86137
"""

class TreeNode():
    def __init__(self, val, left = None , right = None):
        self.root = val
        self.left = left
        self.right = right

def bfs(trees):
    q = -1
    queue = [(trees[0], 0)]
    result = []
    last_t = None
    while queue:
        cur_t, cur_q = queue.pop(0)
        if not q == cur_q and last_t:
            q = cur_q
            result.append(last_t.root)
        last_t = cur_t
        if cur_t.left:
            queue.append((trees[cur_t.left-1], cur_q + 1))
        if cur_t.right:
            queue.append((trees[cur_t.right-1], cur_q + 1))
    result.append(cur_t.root)
    return result
        
N = int(input())
trees = [0]*N
for idx in range(N):
    trees[idx] = TreeNode(str(idx+1))
    left, right = map(int,input().split())
    trees[idx].left = left if not left == -1 else None
    trees[idx].right = right if not right == -1 else None
print(' '.join(bfs(trees)))