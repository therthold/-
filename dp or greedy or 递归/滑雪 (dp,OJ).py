# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:51:01 2024

@author: 86137
"""

order = [[-1,0], [1,0], [0,-1], [0,1]] ## 滑雪动作（方向）
dp = [] ## 储存路径地图
Map = [] ## 储存高度地图
## 每次ski函数的执行必然返回对应单元格的最长子路径
def ski(row, col, dp, order, Map):
    ## 遇到已经找到了最长路径的单元格则直接返回
    if dp[row][col] > 1:
        return dp[row][col]
    else:
        for ac in order:
            ## 判断会不会滑出地图
            if row+ac[0] < 0 or row+ac[0] >= len(Map) or col+ac[1] < 0 or col+ac[1] >= len(Map[0]):
                pass
            ## 路径+1条件，即可不可以滑过去
            elif Map[row][col] > Map[row+ac[0]][col+ac[1]]:
                ## 每个动作遍历一遍，从上下左右找到最长路径然后+1
                dp[row][col] = max(dp[row][col], ski(row+ac[0], col+ac[1], dp, order, Map)+1)
            ## 每个动作遍历后返回找到的最长路径，如果上述elif不成立，即它是四周最低的，那就返回初始值1
        return dp[row][col]
    
R, C = map(int,input().split())
result = 0
for _ in range(R):
    Map.append(list(map(int,input().split())))
    dp.append([1]*C)
## 对每个单元格遍历一遍，找到最长路径即可
for row in range(R):
    for col in range(C):
        ## 对求得的每个单元格的最长路径的集合取最大值
        result = max(result, ski(row, col, dp, order, Map))
print(result)
    