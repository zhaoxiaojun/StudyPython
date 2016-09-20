#coding=utf8
#Matplotlib里的常用类的包含关系为:
#Figure -> Axes -> (Line2D, Text, etc.)
#一个Figure对象可以包含多个子图(Axes)，在matplotlib中用Axes对象表示一个绘图区域，可以理解为子图
import matplotlib.pyplot as plt

def test1():
    # for idx, color in enumerate("rgbyck"):
    #     plt.subplot(321+idx, axisbg=color)

    plt.subplot(221, axisbg='r')
    plt.subplot(222, axisbg='b')
    plt.subplot(212, axisbg='g')
    plt.show()



def test11():
    plt.figure('plot_name',figsize=(10,8),dpi=80)
    #plt.subplots_adjust(left=0.08,right=0.95,bottom=0.05,top=0.95,hspace=0.75)
    subplt = plt.subplot(2,2,2)
    subplt.set_title('title: hello world')
    x = (1,2)
    y = (3,4)
    subplt.plot(x,y,color='r',linewidth=1.5,linestyle='-',label='label1')
    subplt.legend()
    subplt.set_ylim(0, 6)
    subplt.set_xlim(0, 6)
    subplt.set_xlabel('x_label',{'color':'b','position':(1.0,1.0)})
    subplt.set_ylabel('y_label',{'color':'b'})
    subplt.grid(True) #显示网格
    plt.show()





"""
subplot将整个绘图区域等分为numRows行*numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号，
左上的子区域的编号为1。如果numRows，numCols和plotNum这三个数都小于10的话，可以把它们缩写为一个整数，
例如subplot(323)和subplot(3,2,3)是相同的。subplot在plotNum指定的区域中创建一个轴对象。如果新创建的轴和之前创建
的轴重叠的话，之前的轴将被删除

subplot()返回它所创建的Axes对象，我们可以将它用变量保存起来，然后用sca()交替让它们成为当前Axes对象，并调用plot()在其中绘图
"""

if __name__ == '__main__':
    test11()
