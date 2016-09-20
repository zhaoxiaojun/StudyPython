#coding=utf8
import numpy as np
import matplotlib.pyplot as plt

def test21():
    #plt.figure(1) # 创建图表1
    plt.figure(2) # 创建图表2
    ax1 = plt.subplot(211) # 在图表2中创建子图1
    ax2 = plt.subplot(212) # 在图表2中创建子图2
    x = np.linspace(0, 3, 100)
    for i in xrange(5):
        plt.figure(1)  # 选择图表1
        plt.plot(x, np.exp(i*x/3))

        plt.sca(ax1)   # 选择图表2的子图1
        plt.plot(x, np.sin(i*x))
        plt.sca(ax2)  # 选择图表2的子图2
        plt.plot(x, np.cos(i*x))
    plt.show()



def test22():
    x = [1, 2, 3, 4, 5]# Make an array of x values
    y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
    plt.plot(x, y)# use pylab to plot x and y 折线图 Line plots
    #plt.plot(x, y, 'o')  #散点图 Scatter plots
    plt.show()# show the plot on the screen



if __name__ == '__main__':
    test21()
