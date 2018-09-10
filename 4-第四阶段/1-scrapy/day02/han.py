# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:03:33 2018

@author: Administrator
"""
def move(n,a,b,c):
    # 出口
    if n==1:
        print(a,'--->',c)
    else:
        # 递归的推进
        move(n-1,a,c,b)#将n-1个圆盘移动到b
        move(1,a,b,c)#将a的最后一个圆盘移动后到c
        move(n-1,b,a,c)#将b的n-1个圆盘移动到c
move(3,'a','b','c')   


