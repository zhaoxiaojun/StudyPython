#coding=utf8
import sh
#Glob expansion

#print sh.ls("*.py") #error
print sh.ls(sh.glob("*.py"))
