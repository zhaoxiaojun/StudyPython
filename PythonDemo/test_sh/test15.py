#coding=utf8
from sh import tr, tail
#Advanced piping

for line in tr(tail("-f", "files.list", _piped=True), "[:lower:]", "[:upper:]", _iter=True):
    print(line)
