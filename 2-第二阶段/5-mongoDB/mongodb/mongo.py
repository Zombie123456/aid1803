from pymongo import MongoClient 
import pymongo 

#创建mongo的连接对象
conn = MongoClient('localhost',27017)

#选择要连接的数据库 __getitem__   __setitem__ 
# db = conn.stu 
db = conn['grade']

#选择要链接的集合
# my_set = db.class3
my_set = db['class']

# print(my_set)
# print(dir(my_set))

#插入数据　
# my_set.insert({'name':'张铁林','King':'乾隆'})
# my_set.insert([{'name':'陈道明','King':'康熙'},\
#     {'name':'张国立','King':'康熙'}])

# my_set.insert_many([{'name':'唐国强','King':'雍正'},\
#     {'name':'陈建斌','King':'雍正'}])

# my_set.insert_one({'name':'吴奇隆','King':'四爷'})

# my_set.save({'name':'孙中山','King':'民国'})

#删除操作
#删除所有匹配到的内容
# my_set.remove({'name':'张铁林'})
#删除匹配到的第一条数据
# my_set.remove({'name':'陈道明'},multi = False)
#删除全部数据
# my_set.remove()

#查找　

cursor = my_set.find({},{'_id':0})

# for i in cursor:
#     print(i['name'],'----',i['King'])
#     print(i)

cls = db['class']

# for i in cls.find({'age':{'$lt':20}}):
#     print(i['name'],':',i['age'])

# 通过cursor可以使用find后内容的修饰函数
# print(cursor.count())
# for i in cursor.skip(2).limit(3):
#     print(i) 

# cursor 为迭代的，取值后就不能sort了
# for i in cursor.sort([('name',1)]):
#     print(i)

# print(cursor.next())

#先写出字典表示query然后传入
# dic = {'$or':[{'name':'宝强'},{'age':{'$gt':18}}]}

# for i in cls.find(dic):
#     print(i)

# data = cls.find_one(dic)
# cls.remove(data['_id'])

#修改操作
# my_set.update({'name':'张国立'},\
#     {'$set':{'name':'陈道明'}})

# my_set.update({'name':'郑少秋'},\
#     {'$set':{'King':'乾隆'}},upsert = True)

# my_set.update({'King':'康熙'},\
#     {'$set':{'king_name':'玄烨'}},upsert = False,\
#     multi = True)

# my_set.update_many({'King':'雍正'},\
#     {'$set':{'king_name':'胤禛'}})

# my_set.update_one({'name':'孙中山'},\
#     {'$set':{'name':'张铁林','King':'乾隆'}})

# my_set.find_one_and_delete({'King':'四爷'})


#关闭数据库链接
conn.close()
