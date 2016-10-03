#coding=utf8
from sh import tail
#STDOUT/ERR callbacks


def process_output(line):
    print(line)

p = tail("-f", "/var/log/accountpolicy.log", _out=process_output)
p.wait()



