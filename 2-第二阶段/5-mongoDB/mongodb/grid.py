#获取数据库中gridfs文件
from  pymongo import MongoClient 
#和pymongo模块是绑定的
import gridfs

conn = MongoClient('localhost',27017)
db = conn.grid 

#获取gridfs对象
fs = gridfs.GridFS(db) 

files = fs.find()
print(files)
print(files.count())

# files 为可迭代对象
# 每个迭代值为代表一个存入文件的对象
# 通过对象的属性可以获取文件信息
# for file in files:
#     print(file.filename)

for file in files:
    with open(file.filename,'wb') as f:
        while True:
            #file对象有read接口可以直接从数据库读取内容
            data = file.read(64)
            if not data:
                break 
            f.write(data)
conn.close()


