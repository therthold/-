# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:26:29 2024

@author: 86137
"""

import hashlib

def md5_encrypt(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()
T = int(input())
for _ in range(T):
    s1 = input()
    s2 = input()
    print(['No','Yes'][md5_encrypt(s1) == md5_encrypt(s2)])

