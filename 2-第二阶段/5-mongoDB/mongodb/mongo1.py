from pymongo import MongoClient,IndexModel 

conn = MongoClient('localhost',27017)

db = conn.stu 

my_set = db.class3 
cls = db.class2

# print(dir(my_set))
#索引操作

# index = my_set.ensure_index(name)
# print(index)

#创建符合索引　１表示升序　－１表示降序
# index = my_set.ensure_index\
# ([('name',1),('King',1)])
# print(index)

# #先生产索引对象
# index1 = IndexModel([('name',1),('King',-1)])
# index2 = IndexModel([('king_name',1)])
# #将索引对象使用create_indexes生成索引
# indexes = my_set.create_indexes([index1,index2])
# print(indexes)

#唯一索引
# index = cls.ensure_index\
# ('name',unique = True,sparse:True)

#查看指定集合中的索引
for i in my_set.list_indexes():
    print(i)

# my_set.drop_index('name_1_King_-1')
# print("*****************************")
# for i in my_set.list_indexes():
#     print(i)

#删除所有索引
# my_set.drop_indexes()
# print("*****************************")
# for i in my_set.list_indexes():
#     print(i)

# 聚合操作　

l = [{'$group':{'_id':'$King','count':{'$sum':1}}},\
{'$match':{'count':{'$gt':1}}}]

cursor = my_set.aggregate(l)
for i in cursor:
    print(i)
