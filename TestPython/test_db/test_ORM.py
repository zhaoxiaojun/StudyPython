#coding=utf8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class otest(Base):
    # 表的名字:
    __tablename__ = 'ytest'

    # 表的结构:
    a = Column(String(20),primary_key=True)
    b = Column(String(20))
    c = Column(String(20))
    d = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://write:tc12345@192.168.18.85:3306/ubas_tianchengtest')  #'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
#session = DBSession()
# 创建新User对象:
#new_user = User(id='5', name='Bob')
# 添加到session:
#session.add(new_user)
# 提交即保存到数据库:
#session.commit()
# 关闭session:
#session.close()

# 创建Session:
session = DBSession()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
#user = session.query(User).filter(User.id=='5').one()
user = session.query(otest).filter(otest.a==1).one()

# 打印类型和对象的name属性:
print('type:', type(user))
print('a:', user.a)
print('b:', user.b)
print('c:', user.c)
print('d:', user.d)

# 关闭Session:
session.close()
