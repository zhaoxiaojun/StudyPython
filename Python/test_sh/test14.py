#coding=utf8
from sh import tr
#Buffer sizes

n = 0


for chunk in tr("[:lower:]", "[:upper:]", _in="testing", _iter=True):
    print(chunk)
    n = n + 1
print n



n = 0
for chunk in tr("[:lower:]", "[:upper:]", _in="testing", _iter=True, _out_bufsize=0):
    print(chunk)
    n = n + 1
print n

'''
There are 2 bufsize special keyword arguments: _in_bufsize and _out_bufsize. They may be set to the following values: 0  1  N
'''
