# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:06:43 2024

@author: 86137
"""
## 堆的列表实现
class heap_list(object):
    def __init__(self, List):
        self.heap = sorted(List)
        self.length = len(List)
    
    def getidx(self, relation, idx): ## 获取列表第idx位元素的父节点和左右子节点的索引
        if relation == 'parent':
            return (idx-1)//2
        elif relation == 'left':
            return 2*idx + 1
        elif relation == 'right':
            return 2*idx + 2
    
    def minchild(self, idx): ## 返回值最小的子节点，如果没有则返回None
        if 2*idx + 1 >= self.length:
            return None
        elif 2*idx + 2 >= self.length:
            return 2*idx + 1
        else:
            return [2*idx + 1, 2*idx + 2][self.heap[2*idx + 1] > self.heap[2*idx + 2]]
    
    def up(self, idx): ## 将列表第idx位元素进行上浮
        while idx > 0 and self.heap[idx] < self.heap[self.getidx('parent', idx)]:
            parent_idx = self.getidx('parent', idx)
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
    
    def down(self, idx): ## 将列表第idx位元素进行下沉
        child = self.minchild(idx)
        if not child == None:
            if self.heap[child] < self.heap[idx]:
                self.heap[idx], self.heap[child] = self.heap[child], self.heap[idx]
            if not idx == child:
                self.down(child)
        
    
    def popmin(self): ## 弹出列表最小值
        if self.length == 0:
            return None
        else:
            Min = self.heap[0]
            self.length -= 1
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.down(0)
            return Min
    
    def push(self, val): ## 添加新数据
        self.heap.append(val)
        self.length += 1
        self.up(self.length-1)

n = int(input())
K = heap_list([])
for _ in range(n):
    order = input()
    if order[0] == '1':
        K.push(int(order[2:]))
    elif order[0] == '2':
        print(K.popmin())