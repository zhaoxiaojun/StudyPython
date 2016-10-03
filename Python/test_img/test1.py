#coding=utf8
from PIL import Image

'''
PIL：Python Imaging Library
已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在
PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，可以直接安装使用Pillow

Image实例属性：

format:     以string返回图片档案的格式（JPG, PNG, BMP, None, etc.）；如果不是从打开文件得到的实例，则返回None。
mode:   以string返回图片的模式（RGB, CMYK, etc.）；完整的列表参见 官方说明·图片模式列表
size:   以二元tuple返回图片档案的尺寸 (width, height)
palette:    仅当mode为P时有效，返回ImagePalette示例
info:   以字典形式返回示例的信息


Image实例的方法：

save(f,format=None) 保存 如果f是一个file对象，必须指定format（format codes）

convert(mode)   转换mode

copy()       复制

crop(bbox)  剪切 原图中bbox区域

filter(name)    滤镜 滤镜名字需要import ImageFilter

getbands()  通道的字符串序列 如RGB图返回('R', 'G', 'B')

getbbox()   包含非零区域的最小bbox

getextrema()    最大最小像素点值  单通道图：返回元组(min,max)    多通道图：返回各个通道的元组组成的元组

getpixel(xy)    取像素点值

histogram(mask=None)   统计直方图
单通道图：返回列表[c0, c1, ...]，ci是值为i的像素数
多通道图：a single sequence that is the concatenation of the sequences for all bands
mask参数:a same-sized mask image of mode "1" or "L"(include only those pixels correspond to nonzero pixels in the mask argument)

offset(dx,dy=None)   平移  Returns a new image the same size as the original, but with all pixels rotated dx in the +x direction,and dy in the +y direction.
If dy is omitted, it defaults to the same value as dx.

paste(i2,where,mask=None)   粘贴图片
where参数可以是：
(x,y)坐标对：i2的像素点(0,0)对齐原图中的(x,y)粘贴，i2超过原图边界的部分被抛弃
bbox：i2必须和该bounding box大小一致
None：i2必须和原图大小一致
如果i2的mode和原图不一致，粘贴前会被转换
mask参数：a same-sized mask image of mode "1","L" or “RGBA ”(control which pixels get replaced)

paste(color,box=None,mask=None) 填充颜色 如果box省略，整个图被填充为color色；mask参数同上

point(function) 改变像素点(函数) Returns a new image with each pixel modified.

point(table) 改变像素点(查表) To translate pixels using a table(a sequence of 256n values, where n is the number of bands in the image) lookup

putalpha(band)   改变alpha通道  The pixels of the band image(same-sized,"L" or "1") replace the alpha band(A) of the original image(RGBA) in place.

putpixel(xy, color) 改变单个像素点颜色  Note that this method is relatively slow. For more extensive changes, use paste or the ImageDraw module instead.

resize(size,filter=None)  调整大小

rotate(theta)  旋转（围绕图片中心）  Any pixels that are not covered by rotation of the original image are set to black.

show()  显示图片
On Unix systems, this method runs the xv image viewer to display the image.
On Windows boxes,the image is saved in BMP format and can be viewed using Paint.
This can be useful for debugging.

split()   分离通道
返回各个通道的灰度图组成的元组
Returns a tuple containing each band of the original image as an image of mode "L".
For example, applying this method to an "RGB" image produces a tuple of three images, one each for the red, green, and blue bands.

thumbnail(size,filter=None) 缩略图 Modifies in-place,Preserves aspect ratio

transform(xs, ys, Image.EXTENT, (x0,y0,x1,y1))
Returns a transformed copy of the image. In the transformed image, the point originally at (x0,y0) will appear at (0,0), and point (x1,y1) will appear at (xs, ys).

transform(xs, ys, Image.AFFINE, (a,b,c,d,e,f))  affine变换
The values a through f are the first two rows of an affine transform matrix.
Each pixel at (x,y) in the resulting image comes from position (ax+by+c,dx+ey+f) in the input
image, rounded to the nearest pixel.

transpose(method)   翻转旋转   ROTATE_90/180/270(clockwise), FLIP_TOP_BOTTOM(horizontal), FLIP_RIGHT_LEFT(vertical)
'''

sourceFileName = "tbbb.png"

avatar = Image.open(sourceFileName)

print avatar.format, avatar.size, avatar.mode
print avatar.info

avatar.show()  #查看实例。PIL会将实例暂存为一个临时文件，而后打开它


