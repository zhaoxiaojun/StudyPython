#coding=utf8
import mysql.connector
'''
MySQL官方提供了mysql-connector-python驱动
安装: pip install mysql-connector-python --allow-external mysql-connector-python
'''

conn = mysql.connector.connect(host='192.168.18.85', port=3306, user='write', password='tc12345', database='ubas_tianchengtest', charset='utf8')
cursor = conn.cursor()

#创建user表:
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#插入一行记录，注意MySQL的占位符是%s:
#cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
#print('rowcount =', cursor.rowcount)

#提交事务:
#conn.commit()
#cursor.close()

#运行查询:
cursor = conn.cursor()
cursor.execute('select * from userbasicinfo where UserID = %s', ('00003b76-1fef-44f9-84b9-72cb19151101',))
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()
conn.close()
