#coding=utf8
import glob
#查找符合特定规则的文件路径名

#匹配符："*", "?", "[]": "*"匹配0个或多个字符；"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字


#获取指定目录下的所有图片
f = glob.glob(r"./*.py")
for y in f:
    print y
print ''

#获取当前目录的所有.py文件
print glob.glob(r'./*.py')   #相对路径
print ''


#glob.glob同时获取所有的匹配路径，而glob.iglob一次只获取一个匹配路径
f = glob.iglob(r'./*.py')
print f         #<generator object iglob at 0x00B9FF80>
for py in f:
    print py
