#coding=utf8

#创建生成器方式2：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


def fib(max):
    b = 0
    n = 0
    while n < max:
        b = b + 1
        yield b
        b = b + 2
        n = n + 1
        #return     #生成器中只能放参数为空的return语句

def repeater():
    n = 0
    while True:
        n = (yield n)    #挂起后再次执行yield n时，n接收通过send方法调用传递过来的参数，

if __name__ == '__main__':
    #o = fib(10)
    o = repeater()
    #print o.send(None)
    print o.next()   #就相当于o.send(None)  首次启动
    #print o.send(None)
    #print o.next()
    #print o.next()
    print o.send(1)  #调用send传入非None值前，生成器必须处于挂起状态(至少生成过一次值)，否则将抛出异常。不过，未启动的生成器仍可以使用None作为参数调用send。
    print o.send(223)
    print o.send(None)
    print o.send(353)
    print o.close()   #这个方法用于关闭生成器。对关闭的生成器后再次调用next或send将抛出StopIteration异常
    #print o.send(None)
    #print o.send(1)

    #throw(type, value=None, traceback=None): 这个方法用于在生成器内部（生成器的当前挂起处，或未启动时在定义处）抛出一个异常。
