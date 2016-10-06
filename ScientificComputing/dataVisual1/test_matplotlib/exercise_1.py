#coding=utf8
from pylab import *   # 导入matplotlib的所有内容（nympy可以用np这个名字来使用）

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)  #X是一个numpy数组，包含了从−π到+π等间隔的256个值

C,S = np.cos(X), np.sin(X) #C和S分别是这256个值对应的余弦和正弦函数值组成的numpy数组

plot(X,C)
plot(X,S)

show()

'''
Matplotlib的默认配置都允许用户自定义。你可以调整大多数的默认配置：图片大小和分辨率（dpi）、线宽、颜色、风格、坐标轴、坐标轴以及网格的属性、文字与字体属性等。
不过，matplotlib 的默认配置在大多数情况下已经做得足够好，你可能只在很少的情况下才会想更改这些默认配置
'''
