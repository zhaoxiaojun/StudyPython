#coding=utf8
from PIL import Image, ImageDraw, ImageFont

'''
多行文本转为图片
'''


# text = u"""这是一段测试文本,test 123, 阿斯顿sdsfsdsd
# 速度快解放可视对讲，佛山东副书记sdfsf啊啊啊啊啊
# wwwwwww wwwwwww山东 师范。"""

#每行50个字母
text = u"""asdhfjdueyrtrewqiaushygtfrds dmfghjkiuytrw dbfjguq
2sdhfjdueyrtrewqiaushygtfrds dmfghjkiuytrw dbfjguq
3sdhfjdueyrtrewqiaushygtfrds dmfghjkiuytrw dbfjguq"""

font = ImageFont.truetype("/System/Library/Fonts/YaHei.Consolas.1.12.ttf", 14)

textl = text.split('\n')
lw = font.getsize(textl[0])[0]
lh = font.getsize(textl[0])[1]
print '行宽度：', lw   #400
print '行高度：', lh   #18

im = Image.new("RGB", (500, 80), (255, 255, 255))  #Image设置的宽度为500  高度为80  确保能放下文本
dr = ImageDraw.Draw(im)    #Draw

x, y = 25, 5  #起点
for line in textl:
    dr.text((x, y), line, font=font, fill="#000000")  #绘画中填充文本
    y += lh

im.show()
im.save("test13.jpg")
