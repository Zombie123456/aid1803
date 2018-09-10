# dict.py
import re
import pymysql

db = pymysql.connect("localhost","root","123456",
                      charset="utf8")
cur = db.cursor()
cur.execute("use dict;")
f = open('word.txt')
for line in f:
    l = re.split('[ ]+', line)
    sql = "insert into words values('%s','%s')"%(l[0],' '.join(l[1:]))
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()
cur.close()
db.close()