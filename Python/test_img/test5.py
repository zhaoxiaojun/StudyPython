#coding=utf8
from PIL import Image
import os, sys
'''
图片格式转换
'''

infile = 'tbbb.png'
f, e = os.path.splitext(infile)
outfile = f + ".jpg"

if infile != outfile:
    try:
        Image.open(infile).save(outfile)
    except IOError:
        print "cannot convert", infile
