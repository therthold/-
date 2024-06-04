# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:48:20 2024

@author: 86137
"""

def dfs(chess_board, position, result, num):
    if len(position) == k:
        result += 1
    else:
        for row in range(len(chess_board)):
            for col in range(len(chess_board[row])):
                if col not in position and chess_board[row][col] == '#':
                    position.append(col)
                    result += dfs(chess_board[row+1:], position, 0, num)
                    position.pop()
    return result


n,k = map(int,input().split())
while not n == -1 and not k == -1:
    chess_board = []
    for _ in range(n):
        chess_board.append(input())
    print(dfs(chess_board, [], 0, k))
    n,k = map(int,input().split())
