#coding=utf8
from PIL import Image, ImageDraw

'''
画一段弧

arc(xy, start, end, options) 方法来绘制弧
xy是一个长度为4的列表，用来表示一个bounding box。start和end则是弧的起止角度，单位是 °。其中水平向右的方向为0°，竖直向下的方向为90°，
水平向左的方向为180°，竖直向上的方向为270°

'''

sourceFileName = "tbbb.png"
avatar         = Image.open(sourceFileName)
xSize, ySize = avatar.size

drawAvatar     = ImageDraw.Draw(avatar)

drawAvatar.arc([0, 0, xSize, ySize], 0, 90, fill = (255, 100, 255))

del drawAvatar

avatar.save('tbbb_9.jpg', 'jpeg')
avatar.show()
