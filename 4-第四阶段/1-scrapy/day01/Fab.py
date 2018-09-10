# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:16:19 2018

@author: Administrator
"""

#1，1，2，3，5，8，13，21，34...
#f(n) = f(n-1)+f(n-2) n >= 2
#       1             n >= 0 n为自然数
def Fab(n):
    # 递归调用必须有一个出口
    if n == 0 or n == 1:
        return 1
    # 递归：函数的自身调用,变量必须有变化
    return Fab(n-1)+Fab(n-2)

print(Fab(3))
