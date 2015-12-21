#coding=utf8
from types import MethodType

class Student(object):
    pass

s = Student()

s.name = 'Michael' #动态给实例绑定一个属性
print(s.name)

def set_age(self, age): #定义一个函数
    self.age = age

s.set_age = MethodType(set_age, s) #给实例绑定一个方法
s.set_age(25) #调用实例方法
print s.age



def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)  #给class绑定方法


'''
限制class实例能添加的属性
'''
class Student(object):
    __slots__ = ('name', 'age')   #用tuple定义允许绑定的属性名称
