#coding=utf8
import glob
#匹配符："*", "?", "[]": "*"匹配0个或多个字符；"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字


#获取指定目录下的所有图片
f = glob.glob(r"D:\Code\StudyPython\Algorithms\*.py")
for y in f:
    print y

#获取上级目录的所有.py文件
print glob.glob(r'.\*.py')   #相对路径
