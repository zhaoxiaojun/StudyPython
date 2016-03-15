#coding=utf8

"""
属性操作
C.__getattr__(self, attr) 获取属性；内建getattr()；仅当属性没有找到时调用
C.__setattr__(self, attr, val) 设置属性
C.__delattr__(self, attr) 删除属性
C.__getattribute__(self, attr) 获取属性；内建getattr()；总是被调用
C.__get__(self, attr) （描述符）获取属性
C.__set__(self, attr, val)  （描述符）设置属性
C.__delete__(self, attr)  （描述符）删除属性
"""
class A(object):
    def __init__(self):
        self.value = 1

    def __getattr__(self, name):
        print "call __getattr__"
        try:
            return self.__dict__[name]
        except:
            return "not found"

    def __setattr__(self, name, value):
        print "call __setattr__"
        self.__dict__[name] = value

    def __delattr__(self, name):
        print "call __delattr__"
        del self.__dict__[name]

    def __getattribute__(self, name):
        print "call __getattribute__"
        return self.__dict__[name]

    def __get__(self, name):
        print "call __get__"
        pass
    def __set__(self, name, value):
        print "call __set__"
        pass
    def __del__(self):
        print "call __del__"
        pass

if __name__ == '__main__':
    a = A()
    print getattr(a, "value")
    #print getattr(a, "name")
    #del a.value

"""
A.get/getattr/getattribute区别:
object.getattr(self, name)
当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。

object.getattribute(self, name)
无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用（除非显示调用或引发AttributeError异常）

object.get(self, instance, owner)
如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是访问descriptor的实例，如果不是通过实例访问，而是通过类访问的话，instance则为None。（descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）
"""
