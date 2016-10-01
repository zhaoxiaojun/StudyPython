#coding=utf8
import json
"""
处理自己的数据类型
方法一：自己写转化函数
"""

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return 'Person Object name : %s , age : %d' % (self.name,self.age)

def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst





if __name__  == '__main__':
    p = Person('Peter',22)
    print p
    print ''

    #对象转字典
    d = object2dict(p)
    print d
    print ''

    #字典转对象
    o = dict2object(d)
    print type(o),o
    print ''

    #在json.dumps方法中增加default参数，该参数表示在转化过程中调用指定的函数
    dump = json.dumps(p,default=object2dict)
    print dump
    print ''

    #json.loads方法增加object_hook,指定转化函数
    load = json.loads(dump,object_hook = dict2object)
    print load
    print ''






