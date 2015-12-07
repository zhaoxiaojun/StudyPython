#coding=utf8

#创建Connection时，指定host及port参数
import pymongo
conn = pymongo.MongoClient(host='192.168.18.69',port=27088)

#连接数据库
#db = conn.ChatRoom
db = conn['ups']

#连接聚集
#account = db.Account
#account = db["userlabelquery"]
account2 = db["userlabelquery"]

#查看全部聚集名称
#print 'db.collection_names: ', db.collection_names()

#查看聚集的一条记录
#print db.userlabelquery.find_one({"userId":"test123456-348d74c0-78a9-11e5-9980-b083fe6509c4"})
query_where = {}

query_where['labelIds'] = {'$all':[1010002, 1040002]}
#result = account.find_one(query_where)
#if result is not  None:
#    result = result[u'labelIds']
result2 = account2.find(query_where).count()

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

#查看聚集的字段
#db.Account.find_one({},{"UserName":1,"Email":1})  # {u'UserName': u'libing', u'_id': ObjectId('4ded95c3b7780a774a099b7c'), u'Email': u'libing@35.cn'}
#db.Account.find_one({},{"UserName":1,"Email":1,"_id":0})  {u'UserName': u'libing', u'Email': u'libing@35.cn'}

#查看聚集的多条记录
#for item in db.Account.find():
#    print item
#for item in db.Account.find({"UserName":"libing"}):
#    item["UserName"]

#查看聚集的记录统计
#print 'count: ', account.find().count()   # db.Account.find({"UserName":"keyword"}).count()

#聚集查询结果排序
#db.Account.find().sort("UserName")  #默认为升序
#db.Account.find().sort("UserName",pymongo.ASCENDING)   --升序
#db.Account.find().sort("UserName",pymongo.DESCENDING)  --降序

#聚集查询结果多列排序
#db.Account.find().sort([("UserName",pymongo.ASCENDING),("Email",pymongo.DESCENDING)])

#添加记录
#db.Account.insert({"AccountID":21,"UserName":"libing"})

#修改记录
#db.Account.update({"UserName":"libing"},{"$set":{"Email":"libing@126.com","Password":"123"}})

#删除记录
#db.Account.remove()   #全部删除
#db.Test.remove({"UserName":"keyword"})
