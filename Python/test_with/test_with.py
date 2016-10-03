#coding=utf8

with open("foo.txt") as file:
    data = file.read()
print data
print '\n---------------------\n'


class Sample:
    def __enter__(self):
        print "In \n__enter__()"
        return "Foo"

    def __exit__(self, type, value, trace):
        print "In \n__exit__()"



with Sample() as sample:
    print "sample:",sample


'''
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象
的__exit__()方法：
1. __enter__()方法被执行
2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. __exit__()方法被调用
'''






