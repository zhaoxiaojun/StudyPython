#coding=utf8

class Student(object):
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

'''
@property装饰器就负责把一个方法变成属性调用
'''
class Student2(object):
    @property    #把一个getter方法变成属性，只需要加上@property
    def score(self):
        return self._score

    @score.setter   #装饰器@xxxx.setter，负责把一个setter方法变成属性赋值
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(9999)


s2 = Student()
s2.score = 9999



class Student3(object):
    @property
    def birth(self):         #birth是可读写属性
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):           #age是一个只读属性(只定义getter方法，不定义setter方法就是一个只读属性 )
        return 2015 - self._birth

s3 = Student3()
s3.birth
