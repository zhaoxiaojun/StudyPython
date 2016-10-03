#coding=utf8
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

'''
生成字母验证码图片
'''

def rndChar():
    return chr(random.randint(65, 90))  #随机字母

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))  #随机颜色1

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))  #随机颜色2

#240 x 60
width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype('Arial.ttf', 36)  #创建Font对象

draw = ImageDraw.Draw(image)  #创建Draw对象

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())  #填充每个像素

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())   #4个字母

image = image.filter(ImageFilter.BLUR)  #模糊

image.save('code.jpg', 'jpeg')

