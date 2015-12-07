#coding=utf8
from pipe import *

def feibolaqi(n):
    if n == 0 or n == 1:
        return n
    else:
        return feibolaqi(n-1) + feibolaqi(n-2)

def fibonacci():
    a = b = 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b



print range(5) | add
print range(5) | where(lambda x: x % 2 == 0) | add
print range(10) | where(lambda x: (x % 2 == 0) and (x < 6)) | add
print range(10) | where(lambda x: x % 2 == 0) | where(lambda x: x < 6) | add
print range(10) | where(lambda x: x % 2 == 0) | take_while(lambda x: x < 6) | add

print fibonacci() | where(lambda x: x % 2 == 0) | take_while(lambda x: x < 10000) | add   #求出数列中所有小于10000的偶数和

print fibonacci() | select(lambda x: x ** 2) | take_while(lambda x: x < 10000) | as_list  #需要对元素应用某个函数可以使用select，作用类似于内建函数map；需要得到一个列表，可以使用as_list
