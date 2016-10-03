#coding=utf8
from functools import total_ordering


@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
print dir(Student)


"""
这个装饰器是在python2.7的时候加上的，它是针对某个类如果定义了__lt__、le、gt、__ge__这些方法中的至少一个，使用该装饰器，则会自动的把其他几
个比较函数也实现在该类中。
"""
