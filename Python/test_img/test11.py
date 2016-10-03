#coding=utf8
from PIL import Image, ImageDraw, ImageFont


'''
ImageFont

ImageFont模块中的函数：
Load
ImageFont.load(file)⇒ Font instance
从指定的文件中加载一种字体，该函数返回对应的字体对象。如果该函数失败，将产生IOError异常。

Load_path
ImageFont.load_path(file)⇒ Font instance
和函数load()一样，但是如果没有指定当前路径的话，会从sys.path开始查找指定的字体文件。

Truetype
ImageFont.truetype(file,size) ⇒ Font instance
加载一个TrueType或者OpenType字体文件，并且创建一个字体对象。这个函数从指定的文件加载了一个字体对象，并且为指定大小的字体创建了字体对象。在
windows系统中，如果指定的文件不存在，加载器会顺便看看windows的字体目录下是否存在。这个函数需要_imagingft服务。

ImageFont.truetype(file,size, encoding=value) ⇒ Font instance
加载一个TrueType或者OpenType字体文件，并且使用指定的编码方式创建一个字体对象。通常的编码方式有“unic”（Unicode），“symb”（Microsoft
Symbol），“ADOB”（Adobe Standard），“ADBE”（Adobe Expert）和“armn”（Apple Roman）。

Load_default
ImageFont.load_default()⇒ Font instance
加载一个默认的字体。

------------------------------------------
ImageFont模块的方法：
Getsize
font.getsize(text)⇒ (width, height)
返回给定文本的宽度和高度，返回值为2元组。

Getmask
font.getmask(text,mode=”“) ⇒ Image object
为给定的文本返回一个位图。这个位图是PIL内部存储内存的实例（为Image.core接口模块定义）。如果字体使用了抗锯齿，位图的模式为“L”，且其最大值为
255。否则，它的模式为“1”。可选参数mode用于一些显卡驱动指定自己喜欢的模式；如果为空，渲染器可能会返回任意模式。注意：该模式总是一个字符串。

'''

sourceFileName = "tbbb.png"
avatar = Image.open(sourceFileName)
xSize, ySize = avatar.size

drawAvatar = ImageDraw.Draw(avatar)

fontSize = min(xSize, ySize) // 11
myFont = ImageFont.truetype("/Library/Fonts/SFNSDisplay-Black.otf", fontSize)

drawAvatar.text([0, 0], "hello world!", fill = (255, 0, 0), font = myFont)

del drawAvatar

avatar.save('tbbb_11.jpg', 'jpeg')
avatar.show()
