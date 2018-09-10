#! /usr/bin/python3

#100以内素数
# list=[]
# for i in range(2,101):
#     for j in range(2,i-1):
#         if i%j==0:
#             break
#     else:
#         list.append(i)
# print(list,len(list))

# 练习:
#   给定2个常数n>0,k>=0,求出所有排列组合Cnk,求Ank
# n=int(input('输入一个数n:'))
# k=int(input('输入一个数k:'))
# # 定义阶乘函数
# def jc(num):
#     if num==0 or num==1:
#         return 1
#     else :
#         a=1
#         for i in range(1,num+1):
#             a*=i
#     return a
# Cn=jc(n)//(jc(k)*jc(n-k))
# if n<k or n<=0 or k<0:
#     print('error')
# else :
#     print(Cn)

# 输出helloi,i为几,则输出几次
# a=int(input('please input number:'))
# 用递归函数实现while语句功能
# def pr(self):
#     global i
#     if self<=a:
#         print('hello',self)
#         i+=1
#         return pr(i)
# i=1
# if i<=a:
#     pr(i)
# while语句实现
# i =1
# while i<=a:
#     print('hello',i)
#     i+=1

# year=int(input('输入当前年:'))
# month=int(input('输入当前月:'))
# day=int(input('输入当前日:'))
# if year%4==0 and year%100!=0 or year%400==0:

from PIL import ImageDraw,Image,ImageFont
import random

class Captcha(object):
    def __init__(self,size=(100,40),fontSize=30):
        # self.font = ImageFont.truetype('arial.ttf',fontSize)
        self.font=ImageFont.load_default().font
        self.size = size
        self.image = Image.new('RGBA',self.size,(255,)*4)
        self.texts = self.randNum(5)
 
    def rotate(self):
        rot = self.image.rotate(random.randint(-10,10),expand=0)
        fff = Image.new('RGBA',rot.size,(255,)*4)
        self.image = Image.composite(rot,fff,rot)
 
    def randColor(self):
        self.fontColor = (random.randint(0,250),random.randint(0,250),random.randint(0,250))
 
    def randNum(self,bits):
        return ''.join(str(random.randint(0,9)) for i in range(bits))
 
    def write(self,text,x):
        draw = ImageDraw.Draw(self.image)
        draw.text((x,4),text,fill=self.fontColor,font=self.font)
 
    def writeNum(self):
        x = 10
        xplus = 15
        for text in self.texts:
            self.randColor()
            self.write(text, x)
            self.rotate()
            x += xplus
        return self.texts
 
    def save(self):
        self.image.save('captcha.jpg')

img = Captcha()
num = img.writeNum()
