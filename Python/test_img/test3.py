#coding=utf8
import random
from PIL import Image, ImageFilter

'''
模糊效果
'''

im = Image.open('tccc.jpeg')

im2 = im.filter(ImageFilter.BLUR)  #应用模糊滤镜

im2.save('blur.jpg', 'jpeg')
