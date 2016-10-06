#coding=utf8

"""
尽管str(),repr()和``运算在特性和功能方面都非常相似，事实上repr()和``做的是完全一样的事情，它们返回的是一个对象的“官方”字符串表示，也就是说绝大
多数情况下可以通过求值运算（使用内建函数eval()）重新得到该对象
大多数时候有eval(repr(object)) == object

str()则有所不同，str()致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于eval()求值，但很适合用于print语句输出。需要再次提醒的
是，并不是所有repr()返回的字符串都能够用eval()内建函数得到原来的对象。 也就是说repr()输出对Python比较友好，而str()的输出对用户比较友好，如果
某对象没有适于人阅读的解释形式的话，str()会返回与repr()等同的值
"""

s = 'Hello, world.'

str(s)  #'Hello, world.'

repr(s)  #"'Hello, world.'"


str(0.1)  #'0.1'

repr(0.1)  #'0.1'


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s


hello = 'hello, world\n'
hellos = repr(hello)
print hellos


repr((x, y, ('spam', 'eggs')))
