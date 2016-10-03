#coding=utf8
from PIL import Image

'''
变形与粘贴
将一张图片的左半部分截取下来，左右颠倒之后旋转 180°；将图片的右半边不作更改粘贴到左半部分；最后将修改过的左半部分粘贴到右半部分
'''

imageFName = 'tbbb.png'

def iamge_transpose(image):
    xsize, ysize = image.size  #xsize和ysize图片的宽和高

    xsizeLeft = xsize // 2 # xsizeRight = xsize - xsizeLeft

    boxLeft = (0, 0, xsizeLeft, ysize)
    boxRight = (xsizeLeft, 0, xsize, ysize)
    '''
    盒子是用直角坐标的值在image的画布上框定了一个区域
    Image模块以图片的左上角为直角坐标原点，向右为x轴正方向，向下为y轴正方向。元组中的前两个数，代表区域左上角的坐标值；后两个数代表区域右下角的坐标值
    '''

    boxLeftNew = (0, 0, xsize - xsizeLeft, ysize)
    boxRightNew = (xsize - xsizeLeft, 0, xsize, ysize)

    #左半部分
    partLeft = image.crop(boxLeft).transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)

    #由半部分
    partRight = image.crop(boxRight)

    image.paste(partRight, boxLeftNew)

    image.paste(partLeft, boxRightNew)
    return image


avatar = Image.open(imageFName)

avatar = iamge_transpose(avatar)

avatar.save('tbbb_7.jpg', 'jpeg')

avatar.show()


