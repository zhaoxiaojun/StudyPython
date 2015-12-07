#coding=utf8
def tt():
    for x in xrange(4):
        print 'tt'+str(x)
        yield

def gg():
    for x in xrange(4):
        print 'xx'+str(x)
        yield

t = multitask.TaskManager()
t.add(tt())
t.add(gg())
t.run()


#========================
#用yield模拟线程调度
#========================
def thread1():
    for x in range(4):
        yield  x


def thread2():
    for x in range(4,8):
        yield  x


threads=[]
threads.append(thread1())
threads.append(thread2())

def run(threads):
    for t in threads:
        try:
            print t.next()
        except StopIteration:
            pass
        else:
            threads.append(t)


run(threads)

'''
迭代器是一个对象，该对象实现了next()方法，每次调用next()方法放回一个值，直到结束跑出异常StopIteration
创建迭代器：iter()

生成器是一个特殊函数，调用该函数可以创建一个生成器对象，生成器对象也是可迭代的，可以当做迭代器使用，但还包含迭代器所不具有的
特性，除了next方法，还包含：send（next()等价于send(None)）、throw方法。
创建生成器：
1、特殊函数（yield）形式
2、“元组解析” (x for x in xrange(10))
'''
