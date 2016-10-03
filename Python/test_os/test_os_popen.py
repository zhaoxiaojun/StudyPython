#coding=utf8
import os

res =  os.popen("ifconfig").read().strip()
print res


#可以写复杂的shell命令 相比os.system会阻塞在执行的命令子进程中
#token = os.popen("source ~/userRC;nova credentials|grep id|head -2|tail -1|awk '{print $4}'").read().strip()
