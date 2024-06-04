# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:10:50 2024

@author: 86137
"""
## 每次queen函数的执行结束都是为numlist添加元素，是对numlist的直接修改
def queen(startboard, numlist, row = 0):
    ## startboard储存各行皇后排列，未排列的位置放-1（即原题中的a），第i位储存第i行皇后的列数
    ## numlist储存最后排列
    ## 结束条件：当所有排列都完成后，所遍历的行必然为startboard的长度，此时直接储存即可
    if len(startboard) == row:
        ## 由于row和col从0开始，故最终的数据应当每位都加上1
        numlist.append(int(''.join(map(str,startboard))) + 11111111)
    else:
        ## 第row行皇后所在行的遍历（按列进行）
        for col in range(len(startboard)):
            ## 第row行皇后在第col列
            ## flag作为检测是否符合要求的指标
            startboard[row] = col
            flag = True
            ## 检查这个row行col列皇后是否符合要求（以flag为指标），prerow表示先前第prerow行的皇后
            ## or前语句：判断是否与之前有过的第cul行皇后同列；or后语句：判断是否在对角
            ## 若不符，则计算第row行皇后是否可以在下一列
            ## 若相符，则计算下一行皇后可以在哪一列
            for prerow in range(row):
                if col == startboard[prerow] or (abs(row - prerow) == abs(col - startboard[prerow])):
                    flag = False
                    break
            if flag:
                queen(startboard, numlist, row + 1)
result = []
queen([-1]*8, result)
n = int(input())
for _ in range(n):
    t = int(input())
    print(result[t-1])