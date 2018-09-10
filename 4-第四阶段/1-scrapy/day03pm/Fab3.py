# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:37:43 2018

@author: Administrator
"""

#1，1，2，3，5，8，13，21，34...
#f(n) = f(n-1)+f(n-2) n >= 2
#       1             n >= 0 n为自然数
def fab3(n):    
    # 给斐波那契数列的前两个元素赋初值
    # 同时利用index记录循环进行的下标位置
    index, a, b = 0,0,1 
    while index < n:
        yield b  # 保留当前的函数的上下文（变量及下一条语句执行的位置），
        #进入阻塞等待的状态 
        a, b = b, a+b # 这里b的值等于f(n)
        index += 1
    #return b   

if __name__ == "__main__":
    f = fab3(7)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

