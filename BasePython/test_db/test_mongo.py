#coding=utf8
import pymongo
"""
MongoDB以文档的形式存储数据，这种形式有着相对自由的数据结构。MongoDB是一个"无模式"数据库：同一个集合中的文档通常拥有相同的结构，但是MongoDB中并不强制要求
使用相同结构。在内部，MongoDB以一种称为BSON的类似JSON的二进制形式存储文档。pymongo允许我们以Python字典的形式写和取出文档。
"""


#创建Connection时，指定host及port参数
conn = pymongo.MongoClient(host='192.168.18.69',port=27088)
#conn = pymongo.Connection("mongodb://user:password@staff.mongohq.com:10066")  #使用MongoDB URI来连接


#连接数据库
#db = conn.ChatRoom
db = conn['ups']

#连接集合（表）
#account = db.Account
#account = db["userlabelquery"]
account2 = db["userlabelquery"]

#查看全部集合
#print 'db.collection_names: ', db.collection_names()

#向集合中插入文档（数据）
#account2.insert({"name": "flibnip", "description": "grade-A industrial flibnip", "quantity": 3})

"""
关于_id：
当创建任何文档时，MongoDB都会自动添加这个域。它的值是一个ObjectID，一种保证文档唯一的BSON对象。你可能已经注意到，当我们使用insert方法成功创建一个新的文档时，
这个ObjectID同样被返回了。（当你创建文档时，可以通过给_id键赋值来覆写自动创建的ObjectID值）
"""

#查看集合的一条文档
#print db.userlabelquery.find_one({"userId":"test123456-348d74c0-78a9-11e5-9980-b083fe6509c4"}) #find_one方法返回的值是一个简单的Python字典
query_where = {}
query_where['labelIds'] = {'$all':[1010002, 1040002]}
#result = account.find_one(query_where)
#if result is not  None:
#    result = result[u'labelIds']
result2 = account2.find(query_where).count()  #find方法来获得集合中所有文档的列表

#print type(result)
#print result
#print 'result-labelIds: ',result['labelIds']
print 'result2',result2

print type(result2)
#for item in result2:
#    print type(item)
#    print type(item['labelIds'])
#print result2
#for i in result:
#    print i
#    print i[u'labelIds']

#查看集合的字段
#db.Account.find_one({},{"UserName":1,"Email":1})  # {u'UserName': u'libing', u'_id': ObjectId('4ded95c3b7780a774a099b7c'), u'Email': u'libing@35.cn'}
#db.Account.find_one({},{"UserName":1,"Email":1,"_id":0})  {u'UserName': u'libing', u'Email': u'libing@35.cn'}

#查看集合的多条文档
#for item in db.Account.find():
#    print item
#for item in db.Account.find({"UserName":"libing"}):
#    item["UserName"]

#查看集合的文档统计
#print 'count: ', account.find().count()   # db.Account.find({"UserName":"keyword"}).count()

#集合查询结果排序
#db.Account.find().sort("UserName")  #默认为升序
#db.Account.find().sort("UserName",pymongo.ASCENDING)   --升序
#db.Account.find().sort("UserName",pymongo.DESCENDING)  --降序

#集合查询结果多列排序
#db.Account.find().sort([("UserName",pymongo.ASCENDING),("Email",pymongo.DESCENDING)])

#添加文档
#db.Account.insert({"AccountID":21,"UserName":"libing"})

#修改文档
#db.Account.update({"UserName":"libing"},{"$set":{"Email":"libing@126.com","Password":"123"}})

#删除文档
#db.Account.remove()   #全部删除
#db.Test.remove({"UserName":"keyword"})

