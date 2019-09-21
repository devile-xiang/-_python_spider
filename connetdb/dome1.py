#encoding:utf-8


import pymysql
#写法要规范
conn=pymysql.connect(host='localhost',user='root',password='root',
                     database='pymysql_dome',port=3306)


cursor=conn.cursor()

cursor.execute('select 1')
result=cursor.fetchone()
print(result)


conn.close()