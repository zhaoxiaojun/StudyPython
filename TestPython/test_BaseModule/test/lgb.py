#coding=utf-8
#演示变量作用范围

global z            #使用全局变量
z=1                 #给全局变量赋值
x=99                #x全局变量声明时初始化 
def foo(y):         #y和z在函数中被赋值：局部的
    #局部区域
    z=x+y           #x没被赋值，所以它是全局的
    return z

def bar(y):
    global z
    z=x+y
    return z

print foo(1)       #结果=100
print z            #结果=1 
print bar(1)       #结果=100
print z            #结果=100 