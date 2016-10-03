#coding=utf8
from PIL import Image as img
import os

'''
剪裁图片
'''

crtFile = 'tccc.jpeg'
crtIm = img.open(crtFile)

horizon = 8
vertic  = 1

crtW, crtH = crtIm.size
hStep = crtW // horizon
vStep = crtH // vertic

for i in range(vertic):
    for j in range(horizon):
        crtOutFileName = crtFile[:crtFile.rindex('.')] + '_' + str(i) + '_' + str(j)\
                        + crtFile[crtFile.rindex('.'):].lower()

        box = (j * hStep, i * vStep, (j + 1) * hStep, (i + 1) * vStep)

        cropped = crtIm.crop(box)
        cropped.save(crtOutFileName)
