#coding=utf8
import random
from PIL import Image

'''
图像缩放操作
'''

im = Image.open('tccc.jpeg')   #打开一个图像文件

w, h = im.size   #获得图像尺寸

print('Original image size: %sx%s' % (w, h))

im.thumbnail((w//2, h//2))   #缩放到50%

print('Resize image to: %sx%s' % (w//2, h//2))

im.save('tcc_1.jpg', 'jpeg')  # 把缩放后的图像用jpeg格式保存

