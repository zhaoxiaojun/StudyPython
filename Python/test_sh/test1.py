#coding=utf8
#基本用法

from sh import ifconfig
print(ifconfig())
print('')

import sh
print(sh.ls("/"))
print('')


# same thing as above
from sh import ls
print(ls("/"))
print('')

#sh.google_chrome("http://google.com")

# 执行shell脚本文件
# run = sh.Command("/home/amoffat/run.sh") # Absolute path
# run()


lscmd = sh.Command("ls")  # Absolute path not needed
print(lscmd())
