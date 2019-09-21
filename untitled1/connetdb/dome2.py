#encoding:utf-8


import pymysql
#写法要规范
conn=pymysql.connect(host='localhost',user='root',password='root',
                     database='pymysql_dome',port=3306)


cursor=conn.cursor()

# #插入数据
# sql="""insert into user (username,age,password) values ('克哦',56,'asds878')"""
# cursor.execute(sql)
#
# #提交到数据库执行
# conn.commit()

#变量添加

sql="""insert into user (username,age,password) values (%s,%s,%s)"""

username='spider'
age="31"
password="asd8817"

cursor.execute(sql,(username,age,password))

#提交到数据库执行
conn.commit()

conn.close()