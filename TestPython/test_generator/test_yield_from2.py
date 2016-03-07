#coding=utf8
#yield from仅在Python 3.3以上版本中支持


def B():
    return [1,2,3,4,5,6,7,8]  #返回的是一个可迭代（iterable）的对象b

def A():
    yield from B()  #返回一个generator a

print A()


"""
1、b迭代产生的每个值都直接传递给a的调用者。
2、所有通过send方法发送到a的值都被直接传递给b. 如果发送的 值是None，则调用b的__next__()方法，否则调用b的send 方法。如果对b的方法调用产生StopIteration异常，a会继续 执行yield from后面的语句，而其他异常则会传播到a中，导 致a在执行yield from的时候抛出异常。
3、如果有除GeneratorExit以外的异常被throw到a中的话，该异常 会被直接throw到b中。如果b的throw方法抛出StopIteration， a会继续执行；其他异常则会导致a也抛出异常。
4、如果一个GeneratorExit异常被throw到a中，或者a的close 方法被调用了，并且b也有close方法的话，b的close方法也 会被调用。如果b的这个方法抛出了异常，则会导致a也抛出异常。 反之，如果b成功close掉了，a也会抛出异常，但是是特定的  GeneratorExit异常。
5、a中yield from表达式的求值结果是b迭代结束时抛出的  StopIteration异常的第一个参数。
6、b中的return <expr>语句实际上会抛出StopIteration(<expr>) 异常，所以b中return的值会成为a中yield from表达式的返回值。
"""
