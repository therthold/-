# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:34:29 2024

@author: 86137
"""

def trans_to_post(pre, mid):
    if len(pre) <= 1 and len(mid) <= 1:
        return pre
    else:
        root = pre[0]
        idx = mid.find(root)
        return trans_to_post(pre[1:1+idx], mid[:idx]) + trans_to_post(pre[1+idx:], mid[idx+1:]) + root
    
while True:
    try:
        pre, mid = map(str,input().split())
        print(trans_to_post(pre, mid))
    except EOFError:
        break

