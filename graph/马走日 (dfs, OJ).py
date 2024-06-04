# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:13:22 2024

@author: 86137
"""

def dfs(board, i, j, move, count, result, x, y):
    row = len(board)
    col = len(board[0])
    if i < 0 or j < 0 or i >= row or j >= col:
        return result
    if board[i][j] == 1:
        return result
    else:
        board[i][j] = 1
        count += 1
        if count == row*col:
            result += 1
        else:
            for m in move:
                result = dfs(board, i+m[0], j+m[1], move, count, result, x, y)
        if not i == x or not j == y:
            board[i][j] = 0
            count -= 1
        return result
    
t = int(input())
for _ in range(t):
    n, m, x, y = map(int,input().split())
    board = []
    move = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
    for i in range(n):
        board.append([0]*m)
    print(dfs(board, x, y, move, 0, 0, x, y))