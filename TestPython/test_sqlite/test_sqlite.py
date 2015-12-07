#coding=utf8
import sqlite3
"""
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。

"""

conn = sqlite3.connect('test.db')    #连接到SQLite数据库 数据库文件是test.db  如果文件不存在，会自动在当前目录创建
#conn = sqlite3.connect("E:/test.db")  #允许加路径
'''
打开数据库时返回的对象conn就是一个数据库连接对象,它可以有以下操作:
commit()--事务提交  (如果isolation_level隔离级别默认，那么每次对数据库的操作，都需要使用该命令，你也可以设置isolation_level=None，这样就变为自动提交模式)
rollback()--事务回滚
close()--关闭一个数据库连接
cursor()--创建一个游标
'''

cursor = conn.cursor()   #创建一个Cursor

#cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')    #执行一条SQL语句，创建user表

#cursor.execute('insert into user(id, name) values (\'2\', \'Michael\')')  #插入一条记录
#print 'rowcount: ', cursor.rowcount  #通过rowcount获得插入的行数 返回影响的行数

cursor.execute('select * from user where id=?', '2')   #执行查询语句  ?占位符
#获得查询结果集  通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
values = cursor.fetchall()
print values

cursor.execute('select * from user')
values = cursor.fetchall()
print values



cursor.close()   #关闭Cursor
conn.commit()  #提交事务
conn.close()  #关闭Connection





