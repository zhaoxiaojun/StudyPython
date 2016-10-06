#coding=utf8

class MyClass:
    val1 = 'Value 1'  #val1是类的
    '''
    可采用类来访问类属性，如果实例没有同名的属性的话，也可以用实例来访问
    如果要修改类属性的值，必需要通过类来访问，而不是通过实例。因为任何对实例属性的赋值都会创建一个实例属性（如果不存在的话）并且对其赋值
    '''

    def __init__(self):
        self.val2 = 'Value 2' #val2是实例的不是类的

    @staticmethod
    def staticmd():
        print '静态方法，无法访问val1和val2'

    @classmethod
    def classmd(cls):
        print '类方法，类：' + str(cls) + '，val1：' + cls.val1 + '，无法访问val2的值'


if __name__ == '__main__':
    MyClass.staticmd()
    MyClass.classmd()

'''
静态方法：无法访问类属性和实例属性，相当于一个相对独立的方法，跟类其实没什么关系，换个角度来讲，其实就是放在一个类的作用域里的函数而已，可以被继承
类方法：可以访问类属性，无法访问实例属性， 可以被继承

类的静态方法和类方法都可以直接通过类来访问，也可以使用实例来访问
'''
