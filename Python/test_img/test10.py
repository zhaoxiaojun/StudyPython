#coding=utf8
from PIL import Image, ImageDraw

'''
在图片上写字

text(position, string, options) 方法可以在Image实例上写字
position指定的是文本左上角的顶点，而不是文本中心
可用的options有：
font = ImageFont instance   - 指定字体，接受一个ImageFont的实例
fill = (R, G, B)   - 用于指定线条的颜色，其中R、G、B都是0 – 255的整数

如果要写中文如何处理？
'''

sourceFileName = "tbbb.png"
avatar = Image.open(sourceFileName)
xSize, ySize = avatar.size

drawAvatar = ImageDraw.Draw(avatar)

#drawAvatar.text([0.9 * xSize, 0.1 * ySize - drawAvatar.textsize("3")[1]], "hello world!", fill = (128, 0, 128))
drawAvatar.text([0, 0], "hello world!", fill = (128, 0, 128))

del drawAvatar

avatar.save('tbbb_10.jpg', 'jpeg')
avatar.show()
