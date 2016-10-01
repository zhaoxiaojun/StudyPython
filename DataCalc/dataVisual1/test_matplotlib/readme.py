#coding=utf8
from pylab import *

#Matplotlib里的常用类的包含关系为:
#Figure「图像」 -> Axes「子图」 -> (Line2D, Text, etc.)
#Matplotlib中的「图像」指的是用户界面看到的整个窗口内容。在图像里面有所谓「子图」。子图的位置是由坐标网格确定的，而「坐标轴」却不受此限制，可以放在图像的任意位置

"""
当我们调用plot函数的时候，matplotlib调用gca()函数以及gcf()函数来获取当前的坐标轴和图像；如果无法获取图像，则会调用figure()函数来创建一个——严格地说，
是用 subplot(1,1,1) 创建一个只有一个子图的图像

图形界面中可以按下右上角的X来关闭窗口（OS X 系统是左上角）。Matplotlib也提供了名为close的函数来关闭这个窗口。close函数的具体行为取决于你提供的参数：
不传递参数：关闭当前窗口；
传递窗口编号或窗口实例（instance）作为参数：关闭指定的窗口；
all：关闭所有窗口

"""

#图像
'''
参数      默认值             描述
--------------------------------------------
num         1               图像的数量
figsize     figure.figsize  图像的长和宽（英寸）
dpi         figure.dpi      分辨率（点/英寸）
facecolor   figure.facecolor    绘图区域的背景颜色
edgecolor   figure.edgecolor    绘图区域边缘的颜色
frameon     True                是否绘制图像边缘
'''



#子图
'''
可以用子图来将图样（plot）放在均匀的坐标网格中。用subplot函数的时候，你需要指明网格的行列数量，以及你希望将图样放在哪一个网格区域中。此外，gridspec的功能
更强大，你也可以选择它来实现这个功能
'''


#坐标轴
'''
坐标轴和子图功能类似，不过它可以放在图像的任意位置。因此，如果你希望在一副图中绘制一个小图，就可以用这个功能
'''


#记号
'''
良好的记号是图像的重要组成部分。Matplotlib里的记号系统里的各个细节都是可以由用户个性化配置的。可以用Tick Locators来指定在那些位置放置记号，用
Tick Formatters来调整记号的样式。主要和次要的记号可以以不同的方式呈现。默认情况下，每一个次要的记号都是隐藏的，也就是说，默认情况下的次要记号
列表是空的——NullLocator

为不同需求设计的一些Locators：
NullLocator
IndexLocator
FixedLocator
LinearLocator
MultipleLocator
AutoLocator
LogLocator
'''
