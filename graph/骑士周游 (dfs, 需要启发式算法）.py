# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:57:18 2024

@author: 86137
"""
def check(board, i, j):
    row = len(board)
    col = len(board[0])
    if i < 0 or j < 0 or i >= row or j >= col:
        return False
    else:
        return True

def change(board, i, j, move):
    res_list = []
    for m in move:
        new_i, new_j = i+m[0], j+m[1]
        if not check(board, new_i, new_j) or board[new_i][new_j] == 1:
            pass
        else:
            count = 0
            for n in move:
                if check(board, new_i+n[0], new_j+n[1]) and board[new_i+n[0]][new_j+n[1]] == 0:
                    count += 1
            res_list.append((count, m))
    res_list.sort(key = lambda x: x[0])
    return [y[1] for y in res_list]


def dfs(board, i, j, move, count, result, x, y):
    row = len(board)
    col = len(board[0])
    if i < 0 or j < 0 or i >= row or j >= col or result:
        return result
    if board[i][j] == 1:
        return result
    else:
        board[i][j] = 1
        count += 1
        if count == row*col:
            return True
        newmove = change(board, i, j, move)
        for m in newmove:
            result = dfs(board, i+m[0], j+m[1], move, count, result, x, y)
            if result:
                return True
        if not i == x or not j == y:
            board[i][j] = 0
            count -= 1
        return result

n = int(input())
x, y = map(int,input().split())
board = []
move = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
for i in range(n):
    board.append([0]*n)
judge = dfs(board, x, y, move, 0, False, x, y)
print(['fail','success'][judge])