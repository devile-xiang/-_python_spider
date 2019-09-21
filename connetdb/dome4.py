#encoding:utf-8


import pymysql
#写法要规范
conn=pymysql.connect(host='localhost',user='root',password='root',
                     database='pymysql_dome',port=3306)


cursor=conn.cursor()

#删除数据
# sql="""delete from user where id=%s """
#修改数据
sql="""update user set username=%s  where id=%s """

username='新名字'
id=2
cursor.execute(sql,(username,id))


#提交到数据库执行
conn.commit()

conn.close()