#coding=utf8
import os

res =  os.popen("ifconfig").read().strip()
print res


#可以写复杂的shell命令
#token = os.popen("source ~/userRC;nova credentials|grep id|head -2|tail -1|awk '{print $4}'").read().strip()
