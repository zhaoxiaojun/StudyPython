#coding=utf8

"""
对象值比较
C.__cmp__(self, obj)     对象比较；内建cmp()
C.__lt__(self, obj) and C.__le__(self,obj)      小于/小于或等于；对应<及<=操作符
C.__gt__(self, obj) and C.__ge__(self,obj)      大于/大于或等于；对应>及>=操作符
C.__eq__(self, obj) and C.__ne__(self,obj)      等于/不等于；对应==,!=及<>操作符

"""

class A(object):
    def __init__(self, value):
        self.value = value

    def __cmp__(self, obj):
        print "call __cmp__"
        return self.value - obj.value

    def __lt__(self, obj):
        print "call __lt__"
        return self.value < obj.value

    def __gt__(self, obj):
        print "call __gt__"
        return self.value > obj.value

    def __eq__(self, obj):
        print "call __eq__"
        return self.value == obj.value

if __name__ == '__main__':
    a1 = A(1)
    a2 = A(2)
    print cmp(a1,a2)
    #print a1 < a2
    #print a1 > a2
    #print a1 == a2
