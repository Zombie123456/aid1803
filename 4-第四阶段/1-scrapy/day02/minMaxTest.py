# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:23:49 2018

@author: Administrator
"""
def minMax(L):
    # 对输入参数进行,可以使用assert断言
    assert(len(L) > 0)
#    if len(L) <= 0:
#        print("Input Error")
#        return None 
    
    # 在参数合法的情况下，做真正的逻辑  
    # 返回一个合法的输出值
    return myMinMax(L, 0, len(L)-1)

def myMinMax(L, start, end):
   """
   返回一个元组，用来记录List的最大值和最小值
   """
   # (start+end)/2 -> start+(end-start)/2
   if end-start <= 1:
       return (max(L[start],L[end]), 
			   min(L[start],L[end]))
   else:
       #把L分成两部分，分别调用这个方法minMax 
       # 得到(max1,min1)和(max2,min2)
       max1,min1 = myMinMax(L, start, (start+end)//2)
       max2,min2 = myMinMax(L, (start+end)//2+1, end)
       # 比较max1,max2可以得到最终的最大值，
       # 比较min1,min2可以得到最终的最小值，
       return (max(max1,max2), min(min1, min2))

# Test Case
L = [3,4,-1,23,7,8,9,-12,26,28]
print(minMax(L))