# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:15:54 2024

@author: 86137
"""

def operate(op1, op, op2):
    op1 = op1 == 'V'
    op2 = op2 == 'V'
    if op == '|':
        return ['F','V'][op1 or op2]
    elif op == '&':
        return ['F','V'][op1 and op2]
    elif op == '!':
        return ['F','V'][not op1]

def count(stack, op):
    if stack == []:
        stack.append(op)
    elif len(stack) < 2 and stack[-1] != '!':
        stack.append(op)
    else:
        while stack and stack[-1] in '!|&':
            if stack[-1] == '!':
                op = operate(op, stack.pop(), '')
            elif stack[-1] in '|&':
                op = operate(op, stack.pop(), stack.pop())
            if stack == []:
                break
        stack.append(op)
    return stack

while True:
    try:
        judge = input()
        stack = []
        for i in judge:
            if i == 'V' or i == 'F':
                stack = count(stack, i)
            elif i == ')':
                re = stack.pop()
                stack.pop()
                stack = count(stack, re)
            elif i in '(|&!':
                stack.append(i)
        print(stack[0])
    except EOFError:
        break
