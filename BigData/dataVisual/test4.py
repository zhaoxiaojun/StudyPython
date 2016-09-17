#coding=utf8
import numpy as np
import pylab as pl


def test41():
    x = [1, 2, 3, 4, 5, 7]# Make an array of x values
    y = [1, 4, 9, 16, 25, 30]# Make an array of y values for each x value
    pl.plot(x, y)# use pylab to plot x and y
    pl.title('Plot of y vs. x')# give plot a title
    pl.xlabel('x axis')# make axis labels
    pl.ylabel("y axis")
    pl.xlim(0.0, 7.0)# set axis limits  轴坐标限度
    pl.ylim(0.0, 30.)
    pl.show()# show the plot on the screen

def test42():
    x1 = [1, 2, 3, 4, 5]# Make x, y arrays for each graph
    y1 = [1, 4, 9, 16, 25]
    x2 = [1, 2, 4, 6, 8]
    y2 = [2, 4, 8, 12, 16]
    pl.plot(x1, y1, "r")# use pylab to plot x and y
    pl.plot(x2, y2, "g")
    pl.title("Plot of y vs. x")# give plot a title
    pl.xlabel("x axis")# make axis labels
    pl.ylabel("y axis")
    pl.xlim(0.0, 9.0)# set axis limits
    pl.ylim(0.0, 30.)
    pl.show()# show the plot on the screen

def test43():
    x1 = [1, 2, 3, 4, 5]# Make x, y arrays for each graph
    y1 = [1, 4, 9, 16, 25]
    x2 = [1, 2, 4, 6, 8]
    y2 = [2, 4, 8, 12, 16]
    plot1 = pl.plot(x1, y1, 'r')# use pylab to plot x and y : Give your plots names
    plot2 = pl.plot(x2, y2, 'go')
    pl.title('Plot of y vs. x')# give plot a title
    pl.xlabel('x axis') # make axis labels
    pl.ylabel('y axis')
    pl.xlim(0.0, 9.0)    # set axis limits
    pl.ylim(0.0, 30.)
    # pl.legend((plot1, plot2), ('red line', 'green circles'), 'upper left', numpoints=1)   # make legend 图例Figure legends
    pl.show()# show the plot on the screen


if __name__ == '__main__':
    test43()
