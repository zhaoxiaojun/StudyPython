#coding=utf8
import sh
#Multiple arguments 多参数

lscmd = sh.Command("ls")
print lscmd("-l", "/")


# sh.tar("cvf", "/tmp/test.tar", "/my/home/directory/")
# tarcmd = sh.Command("/bin/tar")
# print tarcmd("cvf", "/tmp/test.tar", "/my/home/directory/")
