#求10的算数平方根
c=10
#趋近的方法求平方根
# def square_root_1(c):
#     i=g=0
#     for j in range(0,c+1):
#         if (j*j > c and g == 0):
#             g=j-1
#     while (abs(g*g-c) > 0.0001):
#         g+=0.00001
#         i+=1
#         print('%d:%.5f' % (i,g))
# square_root_1(c)

#二分法求算数平方根
# def square_root_2(c):
#     m_max=c
#     m_min=i=0
#     g=(m_max+m_min)/2
#     while abs(g*g-c) > 0.00000000001:
#         if(g*g < c):
#             m_min=g
#         else:
#             m_max=g
#         g=(m_max+m_min)/2
#         i+=1
#         print('%d:%.13f' % (i,g))
# square_root_2(c)

#用切线的方法求算数平方根
def square_root_3(c):
    g=c/2
    i=0
    while abs(g*g-c) > 0.00000000001:
        g=(g+c/g)
        i+=1
        print('%d:%.13f' % (i,g))
square_root_3(c)
 