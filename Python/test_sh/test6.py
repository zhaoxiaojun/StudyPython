#coding=utf8
from sh import ls
#Redirection 重定向


ls(_out="files.list")

ls("nonexistent", _err="error.txt")

