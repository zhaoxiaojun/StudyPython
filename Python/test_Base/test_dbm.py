#coding=utf8
'''
在一些python小型应用程序中，不需要关系型数据库时，可以方便的用持久字典来存储名称/值对，它与python的字典非常类似，主要区别在于数据是在磁盘读取
和写入的。另一个区别在于dbm的键和值必须是字符串类型
'''
import dbm

#open existing file
db = dbm.open('testdbm', 'w')

#add item
db['first_data'] = 'Hello world'

#verify the previous item remains
if db['first_data'] != None:
    print('the data exists')
else:
    print('Missing item')

#iterate over the keys, may be slow
for key in db.keys():
    print("Key=",key," value=",db[key])

#delete item
del db['first_data']

#close and save to disk
db.close()
