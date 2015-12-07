#coding=utf8
#演示可变参数函数
#!/usr/bin/python

def f1(a,b): print a,b
def f2(a,*b): print a,b
def f3(a,**b): print a,b
def f4(a,*b,**c): print a,b,c
def f5(a,b=2,c=3): print a,b,c
def f6(a,b=2,*c): print a,b,c

f1(1,2)
f1(b=2,a=1)
f2(1,2,3,4)
f3(1,x=2,y=3,z=4)
f4(1,x=2,y=3)
f5(1)
f5(1,4)
f6(1)
f6(1,3,4,5,4)


def echoo(*args,**kwargs):
    print args,kwargs

echoo(1,2,a=3,b=4)

pargs = (1,2)
pkwargs = {'a':3,'b':4}
apply(echoo,pargs,pkwargs)

