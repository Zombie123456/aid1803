import re

pattern = r'((?P<word>ab)c(?P<test>de)f)'

# 获取正则表达式对象
obj = re.compile(pattern)

# 匹配目标字符串获取返回值列表
l = obj.findall('abcdefabcdefgh')
# print(l)

# 以一个或者多个空字符切割字符串
l1 = re.split(r'\s+',
              'hello world nihao   China')
# print(l1)

# 讲目标字符串大写字母替换为＃＃
s = re.sub(r'[A-Z]', '##',
           'Hi,Jame.It is a fine day')
# print(s)

# 返回值多一个实际替换几处
s = re.subn(r'[A-Z]', '$$',
            'Hi,Jame.It is a fine day')
# print(s)

# print(obj.groupindex)
# print(obj.groups)
