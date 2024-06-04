# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:08:47 2024

@author: 86137
"""
## 出队与入队对于每个元素只有一次，故复杂度为O(2n)，关键思想在于维护最大有序列表的存在
import collections

n,k = map(int,input().split())
numlist = list(map(int,input().split()))
result = []
if n <= k:
    print(max(numlist))
else:
    deque = collections.deque()
    for i in range(k):
        while deque and deque[-1] < numlist[i]:
            deque.pop()
        deque.append(numlist[i])
    result = [str(deque[0])]
    for i in range(k,n):
        if deque[0] == numlist[i-k]:
            deque.popleft()
        while deque and deque[-1] < numlist[i]:
            deque.pop()
        deque.append(numlist[i])
        result.append(str(deque[0]))
    print(' '.join(result))