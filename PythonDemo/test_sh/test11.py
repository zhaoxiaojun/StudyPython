#coding=utf8
from sh import tail
#Iterating over output


# runs forever
for line in tail("-f", "/var/log/accountpolicy.log", _iter=True):
    print(line)


