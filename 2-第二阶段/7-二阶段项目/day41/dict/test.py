# test.py
import pymysql

db = pymysql.connect("localhost","root","123456",
                      charset="utf8")
cur = db.cursor()
cur.execute("use dict;")
cur.execute("select * from hist \
             where name='%s';"% 'li' )
data = cur.fetchall()
l=[]
s = ''
for i in data:
    l += i
j=0
for i in range(len(data)):
    s += l[i+j] + '  ' + l[i+1+j] + '  ' + '%s' % l[i+2+j] + '  '
    # print('name:', l[i+j],'word:', l[i+1+j],'time:', l[i+2+j])
    j += 2
print(s)
l1 = s.split('  ')
print(l1)