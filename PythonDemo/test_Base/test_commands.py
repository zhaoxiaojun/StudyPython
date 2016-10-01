#coding=utf8
import commands

#执行命令行 其实也是对os.popen的封装
'''
commands.getstatusoutput(cmd) 返回(status, output).
commands.getoutput(cmd) 只返回输出结果
commands.getstatus(file) 返回ls -ld file的执行结果字符串，调用了getoutput，不建议使用此方法
'''


var = commands.getoutput("ifconfig")
#getstatusoutput( )方法除了可以获取shell命令的执行结果以外还可以获取shell命令执行成功与否
#var = commands.getstatusoutput("ifconfig")

#print var


print commands.getstatusoutput('ls /bin/ls')
print commands.getoutput('ls /bin/ls')
print commands.getstatus('/bin/ls')
