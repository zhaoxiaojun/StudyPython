#coding=utf8
import matplotlib.pyplot as plt

#图像保存为PDF文件

X1 = range(0, 50)
Y1 = [num**2 for num in X1]     #y = x^2
X2 = [0, 1]
Y2 = [0, 1]     #y = x

Fig = plt.figure(figsize=(8,4))  #Create a `figure' instance
Ax = Fig.add_subplot(111)      #Create a `axes' instance in the figure
Ax.plot(X1, Y1, X2, Y2)     # Create a Line2D instance in the axes

Fig.savefig("test3.pdf")
