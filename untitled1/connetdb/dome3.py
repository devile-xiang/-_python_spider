#encoding:utf-8


import pymysql
#写法要规范
conn=pymysql.connect(host='localhost',user='root',password='root',
                     database='pymysql_dome',port=3306)


cursor=conn.cursor()

#查询数据
sql="""select username,age,age from user """

cursor.execute(sql)

#返回一条,每次返回一条，下一次返回下一条
# rusult=cursor.fetchone()

#返回全部满足条件得数据
# rusult=cursor.fetchall()

#返回你想获得条数的的数据
rusult=cursor.fetchmany(2)

print(rusult)

#提交到数据库执行
conn.commit()

conn.close()