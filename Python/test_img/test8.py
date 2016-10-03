#coding=utf8
from PIL import Image, ImageDraw
'''
ImageDraw模块提供了Draw类，它能在Image实例上进行简单的2D绘图。当然复杂的绘图动作是由简单的动作合成而得的，理论上这些动作ImageDraw模块也能做，
只是相对复杂。如果想在Image实例上做复杂的绘图动作，最好是自行对ImageDraw模块提供的各种方法做一些封装
'''

'''
绘制直线

line(xy, options) 方法绘制直线
其中xy表示坐标列表，其形式可以是：
[(x1, y1), (x2, y2), ...] - 包含若干个元组的列表
[x1, y1, x2, y2, ...] - 按照顺序包含坐标信息的列表
[x1, y1, (x2, y2), ...] - 以上两种情况的混合
((x1, y1), (x2, y2), ...) - 包含若干个元组的元组
(x1, y1, x2, y2, ...) - 按照顺序包含坐标信息的元组
(x1, y1, (x2, y2), ...) - 以上两种情况的混合

options中可用的选项有：
fill = (R, G, B) - 用于指定线条的颜色，其中 R、G、B 都是 0 – 255 的整数
width = integer - 用于指定线条的宽度，单位是像素

'''

sourceFileName = "tbbb.png"
avatar = Image.open(sourceFileName)
xSize, ySize = avatar.size

drawAvatar = ImageDraw.Draw(avatar)

drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],fill = (255, 100, 0), width = 3)

drawAvatar.line([0, 0.67 * ySize, xSize, 0.67 * ySize],fill = (255, 0, 0), width = 3)

del drawAvatar

avatar.save('tbbb_8.jpg', 'jpeg')

avatar.show()


