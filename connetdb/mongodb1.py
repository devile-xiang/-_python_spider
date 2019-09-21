#encoding:utf-8

import pymongo
#获取连接对象

client=pymongo.MongoClient("127.0.0.1",port=27017)
#获取数据库
db = client.zhihu

#获取数据库中的集合，（也就是数据库中的表）
collection=db.qa


#写入数据

mydict = {"name":"xiangyong","age":"1314"}

result=collection.insert(mydict)

#插入一条数据


#插入多条数据

# collection.insert_many([{
#     "username":"xiang00",
#     "age":"8989"
# },{
#     "user":"admin",
#     "pwd":"123"
# }]
# )
#find获取集合中的所有数据
# cursor=collection.find()



#获取集合中的一条数据
# result=collection.find_one({"age":"1314"})
# print(result)


#更新数据一条数据
# collection.update_one({"name":"asdasd"},{"$set":{"age":"6666"}})
#更新数据多条数据
# collection.update_many({"name":"asdasd"},{"$set":{"age":"77777"}})

#删除一条数据
# collection.delete_one({"username":"xiang00"})
#删除多条数据
collection.delete_many({"name":"xiangyong"})


#
# for x in cursor:
#     print(x)


#
# print(result)