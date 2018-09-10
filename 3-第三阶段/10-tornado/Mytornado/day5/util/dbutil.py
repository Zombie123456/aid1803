import pymysql

class DBUtil:
    def __init__(self, *args, **kwargs):
        user = kwargs.get('user','root')
        password = kwargs.get('password','123456')
        port = kwargs.get('port',3306)
        database = kwargs.get('database','db_blog')
        host = kwargs.get('host','localhost')
        charset = kwargs.get('charset','utf8')
        connection = pymysql.connect(user=user,
                                     password=password,
                                     port=port,
                                     database=database,
                                     host=host,
                                     charset=charset)
        if connection:
            self.cursor = connection.cursor()
        else:
            raise Exception('数据库连接参数有误!')
    
    def is_login(self,username,password):
        sql='select user_name from tb_user where user_name = %s \
            and user_password = %s'
        params = (username,password)
        num = self.cursor.execute(sql,params)
        if num:
            return True
        else:
            return False
    
    def save_user(self,uname,upwd,avatar,ucity):
        sql = 'insert into tb_user\
            (user_name,user_password,user_avatar,user_city)\
            values(%s,%s,%s,%s)'
        params = (uname,upwd,avatar,ucity)
        try:
            self.cursor.execute(sql,params)
            self.cursor.connection.commit()
        except Exception as e:
            err = str(e)
            r = 'dberror'
            code = err.split(',')[0].split('(')[1]
            if code == '1062':
                r = '用户名已存在'
            raise Exception(r)
    
    def get_blogs(self):
        sql='''select user_name,user_avatar,blog_title,tc,c,blog_content
            from (select comment_blog_id,count(*)c from tb_comment
            group by comment_blog_id)t3
            right join (select user_name,user_avatar,blog_id,blog_title,tc,blog_content
            from tb_user
            join (select blog_id,blog_title,tc,blog_user_id,blog_content
            from tb_blog
            left join (
            select rel_blog_id, group_concat(tag_content)tc
            from tb_tag
            join (select rel_blog_id,rel_tag_id from tb_blog_tag)t
            on tag_id = rel_tag_id
            group by rel_blog_id)t1
            on blog_id = rel_blog_id)t2
            on user_id = blog_user_id)t4
            on comment_blog_id = blog_id'''
        self.cursor.execute(sql)
        blogss = self.cursor.fetchall()
        blogs = []
        for i in blogss:
            if not i[3]:
                i[3] = ''
            dit = {
                'author':i[0],
                'title':i[2],
                'content':i[5],
                'tags':i[3],
                'count':i[4],
                'avatar':i[1]
            }
            blogs.append(dit)
        return blogs
    
    def isexists(self,uname):
        sql='select user_name from tb_user where user_name = %s'
        params = (uname,)
        num = self.cursor.execute(sql,params)
        if num:
            return True
        else:
            return False
        
    def avatar(self,uname):
        sql='select user_avatar from tb_user where user_name =%s'
        params = (uname,)
        self.cursor.execute(sql,params)
        r = self.cursor.fetchone()
        print(r)
        if r:
            return r[0]
        else:
            return 'default_avatar.png'

        


    