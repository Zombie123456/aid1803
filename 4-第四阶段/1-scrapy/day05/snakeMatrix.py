# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:44:37 2018

@author: Python
"""

import numpy as np

# 得到一个整形值的输入，等待生成n*n的矩阵
n = int(input("请输入n的值:"))

# n=4时
# 10 ->  1
# 9  0 0 2
# 8  0 0 3
# 7  6 5 4

# -000000000000000　
# 2^15
myArray = np.zeros((n,n), dtype=np.int16)

# 需要推进循环和赋值变量
num = 1
i = 0    #记录行
j = n-1  #记录列
myArray[i][j] = 1

# num的值用来记录1 -> n*n的
# 变化过程，是大循环退出的条件
while (num < n*n):
    # 向下，行的变化，不断增加
    while(i+1 < n and myArray[i+1][j] == 0):
        i += 1
        num += 1
        myArray[i][j] = num     
    #　向左，列的变化,不断减少
    while(j-1 >= 0 and myArray[i][j-1] == 0):
        j -= 1
        num += 1
        myArray[i][j] = num
    # 向上，行的变化，不断减少
    while(i-1 >= 0 and myArray[i-1][j] == 0):
        i -= 1
        num += 1
        myArray[i][j] = num
    #　向右，列的变化,不断增加
    while(j+1 < n and myArray[i][j+1] == 0):
        j += 1
        num += 1
        myArray[i][j] = num
print(myArray) 