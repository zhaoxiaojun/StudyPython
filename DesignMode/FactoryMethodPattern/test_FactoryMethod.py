#coding=utf8
"""
工厂方法模式
定义：定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类
"""

#基类雷锋类，派生出学生类和志愿者类，由这两种子类完成“学雷锋”工作。子类的创建由雷锋工厂的对应的子类完成

class LeiFeng(object):
    def Sweep(self):
        print "LeiFeng sweep"

class Student(LeiFeng):
    def Sweep(self):
        print "Student sweep"

class Volenter(LeiFeng):
    def Sweep(self):
        print "Volenter sweep"



class LeiFengFactory(object):
    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp

class StudentFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Student()
        return temp

class VolenterFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Volenter()
        return temp

if __name__ == "__main__":
    sf = StudentFactory()
    s=sf.CreateLeiFeng()
    s.Sweep()

    sdf = VolenterFactory()
    sd=sdf.CreateLeiFeng()
    sd.Sweep()
