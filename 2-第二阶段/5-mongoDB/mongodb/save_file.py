#将文件以二级制方式存储
from pymongo import MongoClient 
import bson.binary 

conn = MongoClient('localhost',27017)

#数据库不存在则自动创建
db = conn.savefile
my_set = db.image 

# #存储　
# f = open('img.png','rb')
# #讲读取的二进制字节流，变为bson格式的二进制子串
# content = bson.binary.Binary(f.read())
# #插入文档
# my_set.insert({'filename':'img.png','data':content}) 

# 提取文件
#获取到存储文件的文档字典
data = my_set.find_one({'filename':'img.png'})

with open('img.png','wb') as f:
    f.write(data['data'])

conn.close()


