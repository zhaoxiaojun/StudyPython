#coding=utf8
from sh import sort, du, glob, wc, ls
#Piping 管道


# sort this directory by biggest file
#print(sort(du(glob("*"), "-sb"), "-rn"))

# print the number of folders and files in /
print(wc(ls("-l", "/"), "-l"))
