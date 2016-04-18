#coding=utf8

"""
#open(路径+文件名,读写模式)
#读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式如:'rb','wb','r+b'等等

读写模式的类型有：
rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )

"""
#更好的方式
def genertorfile():
    with open('testm/test4.txt', 'w') as fp:
        pass

def writefile(data):
    with open('testm/test4.txt', 'a+') as fp:
        fp.write(data)
        fp.flush()

def readfile():
    with open('testm/test4.txt', 'r') as fp:
        print fp.readline()


genertorfile()
writefile('testdssds1234dfsdf123')
readfile()
