#coding=utf8
import codecs, sys

print '-'*60

#创建utf-8编码器
look  = codecs.lookup("utf-8")

#创建gb2312编码器
look2 = codecs.lookup("gb2312")

a = "我爱北京天安门"

print len(a), a

b = look.decode(a)   #返回的b[0]是数据，b[1]是长度
print b[0], b[1], type(b[0])

#b2 = look.encode(b[0])
b2 = look2.encode(b[0])

print b2[0], b2[1], type(b2[0])
print len(b2[0])
print '-'*60


#用codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
bfile = codecs.open("dddd.txt", 'w+', "utf-8")  #新建的文件的编码为utf8
#bfile = open("dddd.txt", 'w+') #新建的文件的编码为系统默认(windows下非utf8)

bfile.writelines("os.system('ipconfig')")
bfile.flush()
bfile.close()
