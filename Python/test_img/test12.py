#coding=utf8
from PIL import Image, ImageDraw, ImageFont
import pygame
import StringIO

'''
文字转为图片
'''

text = u"这是一段测试文本，test 123。阿斯顿"

im = Image.new("RGB", (300, 50), (255, 255, 255))  #Image实例 宽度为300， 高度为50

dr = ImageDraw.Draw(im)    #绘画实例
font = ImageFont.truetype("/System/Library/Fonts/YaHei.Consolas.1.12.ttf", 14)


dr.text((0, 0), text, font=font, fill="#000000")  #绘画中填充文本


# #使用pyGame渲染点阵字体
# #原理：先将文字用pyGame渲染为图片，将渲染结果保存在一个StringIO对象中，然后再用PIL加载它
# pygame.init()
# font = pygame.font.Font("/System/Library/Fonts/YaHei.Consolas.1.12.ttf", 14)
# rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))

# #pygame.image.save(rtext, "t.gif")
# sio = StringIO.StringIO()  #使用StringIO的好处是，一切操作都是在内存中进行的，不需要先将它保存到硬盘再用PIL读取
# pygame.image.save(rtext, sio)
# sio.seek(0)
# line = Image.open(sio)
# im.paste(line, (10, 5))

im.show()

im.save("test12.png")
