#coding=utf8
import matplotlib.pyplot as plt

"""
subplot将整个绘图区域等分为numRows行*numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1。如果numRows，
numCols和plotNum这三个数都小于10的话，可以把它们缩写为一个整数，例如subplot(323)和subplot(3,2,3)是相同的。subplot在plotNum指定的区域中创建一个
轴对象。如果新创建的轴和之前创建的轴重叠的话，之前的轴将被删除

subplot()返回它所创建的axes对象，我们可以将它用变量保存起来，然后用sca()交替让它们成为当前Axes对象，并调用plot()在其中绘图
"""


plt.subplot(221, axisbg='r')

plt.subplot(222, axisbg='b')

plt.subplot(212, axisbg='g')

plt.show()
