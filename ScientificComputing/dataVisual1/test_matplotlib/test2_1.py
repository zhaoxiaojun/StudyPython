#coding=utf8
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]     #Make an array of x values
y = [1, 4, 9, 16, 25]   #Make an array of y values for each x value

plt.figure(1) # 创建图表1
plt.figure(2) # 创建图表2

#折线图(Line plots)
plt.figure(1)
plt.plot(x, y)   #use pylab to plot x and y

#散点图(Scatter plots)
plt.figure(2)
plt.plot(x, y, 'o')

plt.show()      #show the plot on the screen

