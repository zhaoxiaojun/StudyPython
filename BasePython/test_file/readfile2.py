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

API:
fp.read([size])  #size为读取的长度，以byte为单位
fp.readline([size]) #读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])  #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
fp.write(str)  #把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)  #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
fp.close()  #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。  如果一个文件在关闭后还对其进行操作会产生ValueError
fp.flush()  #把缓冲区的内容写入硬盘
fp.fileno()  #返回一个长整型的”文件标签“
fp.isatty()  #文件是否是一个终端设备文件（unix系统中的）
fp.tell() #返回文件操作标记的当前位置，以文件的开头为原点
fp.next()  #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[,whence]) #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
fp.truncate([size])  #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。

"""
#更好的方式
def genertorfile():
    with open('testm/test4.txt', 'w') as fp:
        pass

def writefile(data):
    with open('testm/test4.txt', 'a+') as fp:
        fp.writelines(data)
        fp.flush()

def readfile():
    with open('testm/test4.txt', 'r') as fp:
        print fp.readline()


genertorfile()
writefile('testdssds1234dfsdf123')
writefile('testdssds1234dfsdf123')
writefile('testdssds1234dfsdf123')
writefile('testdssds1234dfsdf123')
readfile()
