#coding=utf8
'''
python经典(老实)类的搜索方式是按照“从左至右，深度优先”的方式去查找属性
'''

class Oneclass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print self.data

class Twoclass(Oneclass):
    def display(self):
        print "current value is %s" % self.data

class Threeclass(Twoclass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other1):
        self.data = self.data + other1
    def __mul__(self,other2):
        self.data = self.data * other2

object1 = Oneclass()
object1.setdata(1234)
object1.display()


object2 = Twoclass()
object2.setdata(1234)
object2.display()


object3 = Threeclass(12)
object3.display()
object3.setdata(1234)
object3.display()
object3 + 22
object3.display()
object3 * 10
object3.display()
