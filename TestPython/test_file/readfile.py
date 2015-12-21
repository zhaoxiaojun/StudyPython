#coding=utf8
import os

filename = os.getcwd() + "\\test.txt"
fp = open(filename, "r+")

line1 = fp.readline()
print line1



line2 = fp.readline()
print line2

fp.truncate()


line3 = fp.readline()
print line3
