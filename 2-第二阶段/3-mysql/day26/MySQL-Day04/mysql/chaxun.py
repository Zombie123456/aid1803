import pymysql

db = pymysql.connect("localhost","root","123456",
                     charset="utf8")
cur = db.cursor()

sql_select = "show databases;"
cur.execute(sql_select)

# data = cur.fetchone()
# print("fetchone的结果为",data)

# data2 = cur.fetchmany(2)
# print("fetchmany(2)的结果如下:")
# for i in data2:
#     print(i)

data3 = cur.fetchall()
print("fetchall()的结果如下：", data3)
# for i in data3:
#     print(i)

db.commit()
cur.close()
db.close()


















