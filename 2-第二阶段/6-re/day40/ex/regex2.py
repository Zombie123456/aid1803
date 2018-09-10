# regex3.py
import re

# s = 'Hello World'
# l = re.findall('h\w+', s, re.IGNORECASE)
# print(l)

# s = '''hello world
# Hello kitty
# nihao China'''
# l = re.findall('^Hello', s, re.MULTILINE)
# print(l)

s = '''hello world
Hello kitty
nihao China'''
l = re.findall('''(?P<dog>hello) #dog组
\S+ #空格
(world) #第二组
''', s, re.DOTALL)
print(l)
